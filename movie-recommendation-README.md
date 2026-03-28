# 🎬 Movie Recommendation System

A content-based and collaborative filtering movie recommendation system built with Python, using the MovieLens dataset.

---

## 📌 Overview

This project builds a movie recommendation engine that suggests films based on user preferences and movie metadata. It combines **content-based filtering** (movie genres, descriptions) and **collaborative filtering** (user ratings) to generate personalized recommendations.

---

## 🚀 Features

- 🎯 **Content-Based Filtering** — recommends movies similar to ones a user already liked
- 👥 **Collaborative Filtering** — finds patterns across users with similar tastes
- 📊 **EDA on MovieLens Dataset** — genre distribution, rating analysis, popularity trends
- 🔍 **TF-IDF + Cosine Similarity** for content matching
- 📈 Evaluation using RMSE and Precision@K

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas, NumPy | Data manipulation |
| Scikit-learn | TF-IDF, cosine similarity |
| Matplotlib, Seaborn | Visualizations |
| Jupyter Notebook | Development environment |

---

## 📂 Project Structure

```
movie-recommendation-system/
│
├── data/
│   └── movies.csv          # MovieLens dataset
│
├── notebooks/
│   └── recommendation.ipynb  # Full analysis & model
│
├── src/
│   ├── content_based.py    # Content-based filtering logic
│   └── collaborative.py    # Collaborative filtering logic
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Usage

```bash
# Clone the repository
git clone https://github.com/Rishikuber/movie-recommendation-system.git
cd movie-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook notebooks/recommendation.ipynb
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

- [MovieLens 100K Dataset](https://grouplens.org/datasets/movielens/100k/) — 100,000 ratings by 943 users on 1,682 movies

---

## 🔮 Future Improvements

- [ ] Add deep learning-based embedding model (Neural Collaborative Filtering)
- [ ] Build a Streamlit web interface
- [ ] Deploy via FastAPI

---

## 👤 Author

**Rishi Kuber** — [LinkedIn](https://www.linkedin.com/in/rishi-kuber) | [GitHub](https://github.com/Rishikuber)
