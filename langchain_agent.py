"""
langchain_agent.py — Core LangChain CSV agent logic
"""

import os
from langchain_experimental.agents import create_csv_agent
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType


def validate_api_key(api_key: str) -> bool:
    """Quick check that the key looks valid before making an API call."""
    return api_key and api_key.startswith("sk-") and len(api_key) > 20


def get_csv_agent_response(csv_path: str, question: str, api_key: str) -> str:
    """
    Create a LangChain CSV agent and answer the user's question.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file on disk.
    question : str
        Natural language question about the data.
    api_key : str
        OpenAI API key.

    Returns
    -------
    str
        The agent's answer.
    """
    try:
        # Set API key for this call
        os.environ["OPENAI_API_KEY"] = api_key

        # Initialize LLM — gpt-3.5-turbo is cost-effective; swap to gpt-4o for accuracy
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0,
            openai_api_key=api_key
        )

        # Create CSV agent
        agent = create_csv_agent(
            llm=llm,
            path=csv_path,
            agent_type=AgentType.OPENAI_FUNCTIONS,
            verbose=False,
            allow_dangerous_code=True   # Required flag for langchain >= 0.2
        )

        # Run the question
        response = agent.invoke({"input": question})
        return response.get("output", str(response))

    except Exception as e:
        error_msg = str(e)

        if "AuthenticationError" in error_msg or "Incorrect API key" in error_msg:
            return "❌ Authentication failed. Please check your OpenAI API key."
        elif "RateLimitError" in error_msg:
            return "⏳ Rate limit hit. Please wait a moment and try again."
        elif "context_length_exceeded" in error_msg:
            return (
                "📏 The CSV is too large for a single query. "
                "Try filtering the data to fewer rows before uploading."
            )
        else:
            return f"⚠️ Error: {error_msg}"
