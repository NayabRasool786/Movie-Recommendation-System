import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load datasets
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")
links = pd.read_csv("data/links.csv")
tags = pd.read_csv("data/tags.csv")

# Preprocess tags: combine all tags for a movie
tag_data = tags.groupby("movieId")["tag"].apply(lambda x: ' '.join(x)).reset_index()
movies = pd.merge(movies, tag_data, on='movieId', how='left')

# Fill missing tags with empty string
movies['tag'] = movies['tag'].fillna('')

# TF-IDF Vectorizer on tags
vectorizer = TfidfVectorizer(stop_words='english')
tag_matrix = vectorizer.fit_transform(movies['tag'])

# Ratings matrix (collaborative filtering)
movie_user_matrix = ratings.pivot_table(index='movieId', columns='userId', values='rating').fillna(0)
collab_similarity = cosine_similarity(movie_user_matrix)

# Content-based similarity (tags)
tag_similarity = cosine_similarity(tag_matrix)

# Function to recommend using hybrid logic
def get_recommendations(movie_title):
    try:
        movie_idx = movies[movies['title'].str.contains(movie_title, case=False, na=False)].index[0]
        movie_id = movies.loc[movie_idx, 'movieId']
        
        # Index in ratings matrix (collab)
        collab_idx = movie_user_matrix.index.get_loc(movie_id)
        sim_scores_collab = list(enumerate(collab_similarity[collab_idx]))
        
        # Index in tag matrix (content)
        sim_scores_content = list(enumerate(tag_similarity[movie_idx]))

        # Combine scores (simple average)
        combined_scores = [
            (i, (sim_scores_collab[i][1] + sim_scores_content[i][1]) / 2)
            for i in range(len(sim_scores_collab))
        ]
        
        combined_scores = sorted(combined_scores, key=lambda x: x[1], reverse=True)
        
        top_movies = []
        count = 0
        for i, score in combined_scores:
            mid = movie_user_matrix.index[i]
            title = movies[movies['movieId'] == mid]['title'].values
            if len(title) > 0 and title[0] != movies.loc[movie_idx, 'title']:
                imdb_id = links[links['movieId'] == mid]['imdbId']
                link = f"https://www.imdb.com/title/tt{int(imdb_id.values[0]):07d}/" if not imdb_id.empty else "N/A"
                top_movies.append((title[0], link))
                count += 1
            if count >= 5:
                break

        return top_movies
    except Exception as e:
        print(e)
        return []
