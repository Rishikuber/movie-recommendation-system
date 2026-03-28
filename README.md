# 📊 LangChain CSV Data Analyst

A natural language interface for analyzing any CSV file, powered by **LangChain** and **OpenAI GPT**. Ask plain English questions — get instant data insights.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.2-green?style=for-the-badge)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red?style=for-the-badge)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange?style=for-the-badge)](https://openai.com)

---

## 🎯 What It Does

Upload any CSV file and chat with your data in plain English:

> *"What is the total revenue by region?"*
> *"Which product has the highest sales in Q3?"*
> *"Show average discount per sales rep."*
> *"How many orders have quantity greater than 5?"*

The LangChain agent writes Python/Pandas code under the hood and returns a human-readable answer — no SQL, no formulas needed.

---

## 🚀 Demo

![App Demo](assets/demo.gif)

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | OpenAI GPT-3.5 / GPT-4o |
| Agent Framework | LangChain CSV Agent |
| Frontend | Streamlit |
| Data Handling | Pandas, NumPy |

---

## ⚙️ Setup

**1. Clone the repo**
```bash
git clone https://github.com/Rishikuber/langchain-csv-analyst.git
cd langchain-csv-analyst
```

**2. Create a virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Generate sample data (optional)**
```bash
python generate_sample_data.py
```

**5. Run the app**
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 🔑 API Key

This project requires an OpenAI API key.

1. Go to [platform.openai.com](https://platform.openai.com)
2. Create an account and generate an API key
3. Enter the key in the app's sidebar (never commit it to GitHub)

**Estimated cost:** ~$0.01–0.05 per session using GPT-3.5-turbo.

---

## 📂 Project Structure

```
langchain-csv-analyst/
│
├── app.py                    # Streamlit UI
├── langchain_agent.py        # LangChain agent logic
├── generate_sample_data.py   # Generates demo CSV
├── sample_sales_data.csv     # 500-row sales dataset (demo)
├── requirements.txt
└── README.md
```

---

## 💬 Example Questions to Try

With the included **sample sales dataset**:

| Question | What You'll Learn |
|----------|------------------|
| What is total revenue by region? | Regional performance |
| Which product generates the most revenue? | Top product |
| What is the average discount by sales rep? | Rep efficiency |
| How many orders were placed in Q2? | Quarterly volume |
| Show top 5 customers by revenue | Customer ranking |
| What is the month with highest sales? | Seasonal trends |

---

## 🔮 Roadmap

- [ ] Support for multiple CSV uploads
- [ ] Auto chart generation (matplotlib/plotly)
- [ ] Export Q&A history to PDF
- [ ] Add memory for follow-up questions
- [ ] Support local LLMs (Ollama) for free usage

---

## 📚 Key Concepts

- **LangChain CSV Agent** — wraps a Pandas DataFrame with an LLM, enabling natural language queries
- **OpenAI Functions Agent** — uses function calling for structured, reliable output
- **RAG-adjacent** — the agent retrieves relevant data context before generating answers

---

## 👤 Author

**Rishi Kuber** — Data Science Intern @ Zetheta Algorithms

- 🔗 [LinkedIn](https://www.linkedin.com/in/rishi-kuber)
- 🐙 [GitHub](https://github.com/Rishikuber)

---

## 📄 License

MIT License — free to use, modify, and distribute.
