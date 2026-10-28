from pathlib import Path
import sqlite3
import requests
import pandas as pd
import streamlit as st

# Application settings
st.set_page_config(
    page_title="E-commerce Product Assistant",
    page_icon="🛍️",
    layout="centered"
)

PROJECT_DIR = Path(__file__).resolve().parent
DB_PATH = PROJECT_DIR / "notebooks" / "ecommerce.db"
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen2.5:1.5b"


@st.cache_data
def load_products():
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql_query(
            """
            SELECT title, price, rating, stock, availabilityStatus
            FROM products
            """,
            conn
        )


def verified_answer(question, df):
    q = question.lower()

    if any(x in q for x in [
        "highest rating", "highest-rated", "highest rated",
        "best rated", "top-rated", "top rated"
    ]):
        row = df.loc[df["rating"].idxmax()]
        return (
            f"**Highest-rated product: {row['title']}**\n\n"
            f"- Rating: {row['rating']:.2f}/5\n"
            f"- Price: ${row['price']:,.2f}\n\n"
            f"*Verified against {len(df)} products.*"
        )

    if any(x in q for x in [
        "cheapest", "lowest price", "least expensive"
    ]):
        row = df.loc[df["price"].idxmin()]
        return (
            f"**Cheapest product: {row['title']}**\n\n"
            f"- Price: ${row['price']:,.2f}\n"
            f"- Rating: {row['rating']:.2f}/5\n\n"
            f"*Verified against {len(df)} products.*"
        )

    if any(x in q for x in [
        "most expensive", "highest price", "priciest"
    ]):
        row = df.loc[df["price"].idxmax()]
        return (
            f"**Most expensive product: {row['title']}**\n\n"
            f"- Price: ${row['price']:,.2f}\n"
            f"- Rating: {row['rating']:.2f}/5\n\n"
            f"*Verified against {len(df)} products.*"
        )

    if any(x in q for x in [
        "how many products", "total products", "number of products"
    ]):
        return f"There are **{len(df)} products** in the database."

    if "average rating" in q or "average product rating" in q:
        avg = df["rating"].mean()
        return f"The average product rating is **{avg:.2f}/5**."

    return None


def ask_local_llm(question, df, history):
    context = df.to_string(index=False)

    messages = [
        {
            "role": "system",
            "content": (
                "You are an E-commerce Product Intelligence Assistant. "
                "Answer using only the provided product data. "
                "Use simple business language. "
                "Do not invent products or numeric values. "
                "If the data does not support an answer, say so."
            )
        }
    ]

    # Include recent conversation for chat-style interaction.
    for item in history[-6:]:
        if item["role"] in ("user", "assistant"):
            messages.append({
                "role": item["role"],
                "content": item["content"]
            })

    # Add the full product dataset to the current question.
    messages.append({
        "role": "user",
        "content": (
            f"Product data for {len(df)} products:\n{context}\n\n"
            f"Business question: {question}"
        )
    })

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "messages": messages,
            "stream": False
        },
        timeout=180
    )
    response.raise_for_status()
    return response.json()["message"]["content"]


# Page layout
st.title("🛍️ E-commerce Product Assistant")
st.caption("Ask about product ratings, prices, and stock.")

try:
    products_df = load_products()
except Exception as exc:
    st.error(f"Could not load the product database: {exc}")
    st.stop()

st.caption(f"Connected to {len(products_df)} products")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 Ask me about product ratings, prices, "
                "or your e-commerce product data."
            )
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input("Ask a product question..."):
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Checking product data..."):
            answer = verified_answer(question, products_df)

            if answer is None:
                try:
                    answer = ask_local_llm(
                        question,
                        products_df,
                        st.session_state.messages[:-1]
                    )
                except requests.RequestException:
                    answer = (
                        "I could not connect to the local AI model. "
                        "Please check that Ollama is running."
                    )
                except Exception as exc:
                    answer = f"An error occurred: {exc}"

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
