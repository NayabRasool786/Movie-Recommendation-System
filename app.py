import streamlit as st
from utils.recommender import get_recommendations
import base64

# Page configuration
st.set_page_config(page_title="🎬 Mini Netflix Recommender", layout="centered")

# Load external CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Add background image with overlay
def add_bg_with_overlay(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    css = f"""
    <style>
    [data-testid="stAppViewContainer"]::before {{
        content: "";
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        background-image: linear-gradient(rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0.8)), 
                          url("data:image/webp;base64,{encoded_string}");
        background-repeat: no-repeat;
        background-position: center center;
        background-size: cover;
        z-index: 0;
    }}
    [data-testid="stAppViewContainer"] > * {{
        position: relative;
        z-index: 1;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Apply background
add_bg_with_overlay("assets/netflixlogobackground.webp")

# Header
st.markdown('<div class="main-title">🎬 Mini Netflix Recommender</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Get better, smarter movie suggestions 🍿</div>', unsafe_allow_html=True)

# Input
movie_input = st.text_input("Enter a movie name (e.g. Inception)")

# Output
if st.button("Recommend"):
    if movie_input:
        with st.spinner("Finding your next binge..."):
            recommendations = get_recommendations(movie_input)
            if recommendations:
                st.markdown('<div class="recommendation-box">🎥 Recommended Movies:</div>', unsafe_allow_html=True)
                for title, link in recommendations:
                    st.markdown(f'<a href="{link}" target="_blank">{title}</a>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="recommendation-error-box">No recommendations found. Try another movie.</div>', unsafe_allow_html=True)
