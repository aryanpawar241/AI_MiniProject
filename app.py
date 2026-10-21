import streamlit as st
from database import BOOKS
from recommender import recommend_books

# Page Config
st.set_page_config(
    page_title="Book Recommender",
    page_icon="📚",
    layout="centered"
)

st.title("Rule-Based Book Recommendation System")
st.write("Customize your reading preferences in the sidebar to get instant matches!")

# Sidebar Preferences
st.sidebar.header("Your Preferences")

# Added 'motivation' to the options list
genre_choice = st.sidebar.selectbox(
    "Select Genre",
    options=["motivation", "sci-fi", "fantasy", "thriller", "romance"],
    format_func=lambda x: "Motivation / Self-Help" if x == "motivation" else x.title()
)

pace_choice = st.sidebar.selectbox(
    "Select Reading Pace",
    options=["fast", "medium", "slow"],
    format_func=lambda x: f"{x.title()}-paced"
)

length_choice = st.sidebar.selectbox(
    "Select Book Length",
    options=["short", "medium", "long"],
    format_func=lambda x: f"{x.title()} (Short: <300p | Med: 300-450p | Long: >450p)"
)

# Button to trigger recommendation logic
if st.sidebar.button("Get Recommendations", type="primary"):
    user_prefs = {
        "genre": genre_choice,
        "pace": pace_choice,
        "length": length_choice
    }
    
    results = recommend_books(user_prefs, BOOKS)
    
    st.subheader("📖Recommended Books For You")
    
    if not results:
        st.warning("No books matched all your criteria strictly. Try shifting your preferences!")
    else:
        for score, book in results:
            with st.container():
                st.markdown(f"### {book['title']} *by {book['author']}*")
                st.progress(score / 100, text=f"Match Score: {score}%")
                st.caption(f"**Genre:** {book['genre'].title()} | **Pace:** {book['pace'].title()} | **Length:** {book['length'].title()}")
                st.write(book['desc'])
                st.divider()
else:
    st.info("👈 Use the sidebar options and click **Get Recommendations** to view suggestions.")