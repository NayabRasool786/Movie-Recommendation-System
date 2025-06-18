# 🎬 Mini Netflix Movie Recommender (Streamlit App)

##Structure
movie_recommender_app/
├── app.py
├── utils/
│   └── recommender.py
├── data/
│   ├── movies.csv
│   ├── ratings.csv
│   ├── tags.csv
│   └── links.csv
├── assets/
│   ├── backgroundimg.webp
│   └── style.css
├── requirements.txt
└── README.md

This is a beginner-friendly movie recommendation system built using:
- 📊 Pandas + MovieLens Dataset
- 🤖 Cosine Similarity (Scikit-learn)
- 🧪 Streamlit for interactive web interface

## 🔍 How It Works
1. Enter the name of any movie you like
2. It finds similar movies based on user rating patterns
3. Outputs top 5 recommendations instantly!

## 📦 Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
