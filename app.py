"""
app.py — LangChain CSV Data Analyst
Run: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import os
from langchain_agent import get_csv_agent_response, validate_api_key

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LangChain CSV Analyst",
    page_icon="📊",
    layout="wide"
)

# ── Header ─────────────────────────────────────────────────────────────────────
st.title("📊 LangChain CSV Data Analyst")
st.markdown(
    "Upload any CSV file and ask questions in plain English. "
    "Powered by **LangChain** + **OpenAI GPT**."
)
st.divider()

# ── Sidebar: API Key ───────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="sk-...",
        help="Get your key from platform.openai.com"
    )

    st.markdown("---")
    st.markdown("**Example Questions:**")
    st.markdown("- What is the total revenue by region?")
    st.markdown("- Which product has the highest sales?")
    st.markdown("- Show average order value per month")
    st.markdown("- How many customers churned last quarter?")
    st.markdown("- What is the correlation between price and quantity?")

# ── Main: File Upload ──────────────────────────────────────────────────────────
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader(
        "Upload your CSV file",
        type=["csv"],
        help="Max 200MB. Any structured CSV works."
    )

with col2:
    use_sample = st.checkbox("Use sample sales data", value=False)
    if use_sample:
        st.info("📂 sample_sales_data.csv will be loaded")

# ── Load Data ──────────────────────────────────────────────────────────────────
df = None

if use_sample:
    sample_path = "sample_sales_data.csv"
    if os.path.exists(sample_path):
        df = pd.read_csv(sample_path)
        st.success("✅ Sample data loaded!")
    else:
        st.error("sample_sales_data.csv not found. Run: python generate_sample_data.py")

elif uploaded_file:
    df = pd.read_csv(uploaded_file)
    # Save temporarily for LangChain agent
    temp_path = "temp_uploaded.csv"
    df.to_csv(temp_path, index=False)
    st.success(f"✅ File loaded: {uploaded_file.name}")

# ── Preview Data ───────────────────────────────────────────────────────────────
if df is not None:
    st.subheader("📋 Data Preview")

    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Rows", f"{df.shape[0]:,}")
    col_b.metric("Columns", df.shape[1])
    col_c.metric("Missing Values", df.isnull().sum().sum())

    with st.expander("Show first 5 rows", expanded=True):
        st.dataframe(df.head(), use_container_width=True)

    with st.expander("Column Info"):
        info_df = pd.DataFrame({
            "Column": df.columns,
            "Type": df.dtypes.values,
            "Non-Null": df.notnull().sum().values,
            "Unique": df.nunique().values
        })
        st.dataframe(info_df, use_container_width=True)

    st.divider()

    # ── Chat Interface ─────────────────────────────────────────────────────────
    st.subheader("💬 Ask Your Data")

    if not api_key:
        st.warning("⚠️ Enter your OpenAI API key in the sidebar to start chatting.")
    else:
        # Initialize chat history
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat history
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # User input
        if prompt := st.chat_input("Ask anything about your data..."):
            # Validate API key on first use
            if not validate_api_key(api_key):
                st.error("❌ Invalid OpenAI API key. Please check and try again.")
            else:
                # Add user message
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                # Get agent response
                csv_path = "sample_sales_data.csv" if use_sample else "temp_uploaded.csv"

                with st.chat_message("assistant"):
                    with st.spinner("🤔 Analyzing your data..."):
                        response = get_csv_agent_response(
                            csv_path=csv_path,
                            question=prompt,
                            api_key=api_key
                        )
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

        # Clear chat button
        if st.session_state.get("messages"):
            if st.button("🗑️ Clear Chat"):
                st.session_state.messages = []
                st.rerun()

else:
    st.info("👆 Upload a CSV file or check 'Use sample sales data' to get started.")

# ── Footer ─────────────────────────────────────────────────────────────────────
st.divider()
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with LangChain + Streamlit | "
    "<a href='https://github.com/Rishikuber/langchain-csv-analyst'>GitHub</a></p>",
    unsafe_allow_html=True
)
