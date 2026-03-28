# 🎬 Movie Recommendation System

A content-based and collaborative filtering movie recommendation system built with Python, using custom movie, ratings, and user datasets.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

## 📌 Overview

This project builds a movie recommendation engine that suggests films based on user preferences and movie metadata. It combines **content-based filtering** (movie genres, metadata) and **collaborative filtering** (user ratings patterns) to generate personalized recommendations.

---

## 🚀 Features

- 🎯 **Content-Based Filtering** — recommends movies similar to ones a user already liked
- 👥 **Collaborative Filtering** — finds patterns across users with similar tastes
- 📊 **Exploratory Data Analysis** — genre distribution, rating trends, user behavior
- 🔍 **Cosine Similarity** for content matching
- 🤖 Pre-trained recommender model (`recommender_model.py`)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas, NumPy | Data manipulation |
| Scikit-learn | Similarity computation |
| Matplotlib, Seaborn | Visualizations |
| Jupyter Notebook | Development & analysis |

---

## 📂 Project Structure

```
movie-recommendation-system/
│
├── recommendation_system.ipynb   # Full analysis, EDA & model building
├── recommender_model.py          # Recommendation logic & functions
├── main.py                       # Entry point to run recommendations
├── recommender_movies.csv        # Movie metadata (title, genre, etc.)
├── recommender_ratings.csv       # User ratings data
├── recommender_users.csv         # User information
└── README.md
```

---

## ⚙️ Setup & Usage

```bash
# Clone the repository
git clone https://github.com/Rishikuber/movie-recommendation-system.git
cd movie-recommendation-system

# Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn jupyter

# Run the recommender
python main.py

# Or explore the full notebook
jupyter notebook recommendation_system.ipynb
```

---

## 📊 Sample Output

```
Input: User liked "The Dark Knight"
Recommendations:
  1. Batman Begins        (Similarity: 0.92)
  2. Inception            (Similarity: 0.87)
  3. The Prestige         (Similarity: 0.84)
  4. Interstellar         (Similarity: 0.81)
  5. V for Vendetta       (Similarity: 0.78)
```

---

## 📦 Dataset

Custom datasets included in the repo:
- `recommender_movies.csv` — movie titles, genres, metadata
- `recommender_ratings.csv` — user-movie ratings
- `recommender_users.csv` — user demographic info

---

## 🔮 Future Improvements

- [ ] Add deep learning-based Neural Collaborative Filtering
- [ ] Build a Streamlit web interface
- [ ] Deploy via FastAPI
- [ ] Add real-time personalization

---

## 👤 Author

**Rishi Kuber** — Data Science Intern @ Zetheta Algorithms

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rishi-kuber)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/Rishikuber)

---

## 📄 License

MIT License — free to use, modify, and distribute.
