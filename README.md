# 🎬 Mini Netflix Recommendation System
A hybrid movie recommender web app built using **Python**, **Pandas**, **Scikit-learn**, and the **MovieLens latest dataset**, deployed using **Streamlit Cloud**.

---

## Structure
```bash
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
│   ├── netflixlogobackground.webp
│   └── style.css
├── requirements.txt
└── README.md

```

This is a beginner-friendly movie recommendation system built using:
- 📊 Pandas + MovieLens Dataset
- 🤖 Cosine Similarity (Scikit-learn)
- 🧪 Streamlit for interactive web interface

---

## 🧠 Technologies Used
- **Libraries**: `pandas`, `scikit-learn`, `streamlit`
- **Machine Learning**:
  - `cosine_similarity` (collaborative filtering)
  - `TfidfVectorizer` (content-based filtering)
- **Frontend**: HTML + CSS injection via `st.markdown`
- **Deployment**: Streamlit Cloud

---

## 📂 Datasets Used
- `movies.csv`: Movie titles and genres
- `ratings.csv`: User ratings for movies
- `tags.csv`: User-generated tags per movie
- `links.csv`: Maps `movieId` to IMDb and TMDb IDs

---

## 📥 Data Collection & Integration
1. **Grouped tags** by `movieId` using `tags.csv`
2. **Merged** grouped tag data with `movies.csv` using `left join` to align movie metadata with user-generated tags

---

## 🧹 Data Cleaning
- Filled all missing and NA values in tag text with empty strings to avoid vectorization errors
- Ensured all movies had a valid reference to tags or placeholders

---

## 🔄 Hybrid Recommendation Approach
Combined both collaborative and content-based methods:

### 🔹 Content-Based Filtering
- Applied `TfidfVectorizer` on combined user `tags`
- Built a **tag matrix** for each movie

### 🔸 Collaborative Filtering
- Created **rating matrix** from `ratings.csv`
- Calculated similarity using `cosine_similarity` between users/movies

### ⚙️ Hybrid Logic
- Created a function to:
  - Fetch movie index from both matrices
  - Calculate similarity scores from both matrices
  - Average the scores to form a **hybrid recommendation score**
  - Remove duplicates and filter most relevant titles
  - Output **Top 5 movie suggestions** with direct IMDb links

---

## 🖥️ Streamlit Frontend
- Created `app.py` as main entry
- Imported recommendation logic from `recommender.py`
- Used `st.text_input`, `st.button`, and `st.markdown` for UI
- Styled output using **custom HTML & CSS** to create clickable IMDb movie titles

---

## 🚀 Deployment
- Organized entire project in a modular structure
- Created `requirements.txt` with all necessary dependencies
- Successfully deployed on **Streamlit Cloud**

---

## ✅ Outcome
- Simple, powerful recommender system
- Real-time suggestions via Streamlit UI
- Great project for portfolios, resumes, or demos

---


## 🔍 How It Works
1. Enter the name of any movie you like
2. It finds similar movies based on user rating patterns
3. Outputs top 5 recommendations instantly!

---

## 📦 Tech Stack
- Python
- Pandas
- Scikit-learn
- Streamlit

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py 
```
---

## 👨‍💻 Developed By
**Shaik Nayab Rasool**

---

## 🔗 Connect with Me
👋 Hi, I'm **NAYAB RASOOL SHAIK**

[![🔗LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/nayabrasool-shaik)  
[![Email](https://img.shields.io/badge/Email-Send%20Mail-blue?logo=gmail)](mailto:nayabshaik046@example.com)  
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-blueviolet?logo=google-chrome)](http://nayabrasool.my.canva.site/)

> _“Learn deeply, build practically, explain simply, and share widely.” – Shaik Nayab Rasool_
