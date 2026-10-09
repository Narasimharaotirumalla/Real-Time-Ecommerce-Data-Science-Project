
import sqlite3
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="E-Commerce Product Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("E-Commerce Product Intelligence Dashboard")
st.caption("Product performance, inventory value, and stock-risk monitoring")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "notebooks" / "ecommerce.db"


@st.cache_data
def load_data():
    with sqlite3.connect(DB_PATH) as connection:
        return pd.read_sql_query("SELECT * FROM products", connection)


try:
    df = load_data()
except Exception as error:
    st.error(f"Could not load product data: {error}")
    st.stop()

if df.empty:
    st.warning("No product records found in the database.")
    st.stop()

# KPI metrics
total_products = len(df)
total_inventory_value = df["inventory_value"].fillna(0).sum()
average_rating = df["rating"].mean()
low_stock_products = int(df["is_low_stock"].fillna(0).sum())
out_of_stock_products = int(df["is_out_of_stock"].fillna(0).sum())

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Products", f"{total_products:,}")
col2.metric("Inventory Value", f"{total_inventory_value:,.2f}")
col3.metric("Average Rating", f"{average_rating:.2f}/5")
col4.metric("Low Stock Products", f"{low_stock_products:,}")
col5.metric("Out of Stock Products", f"{out_of_stock_products:,}")

st.divider()

# Category filter
st.subheader("Explore Product Inventory")

categories = sorted(df["category"].dropna().unique().tolist())

selected_categories = st.multiselect(
    "Filter by Category",
    options=categories,
    default=categories
)

filtered_df = df[df["category"].isin(selected_categories)]

if filtered_df.empty:
    st.info("Select at least one category to display product data.")
    st.stop()

# Inventory value by category - Vertical Bar Chart
category_inventory = (
    filtered_df.groupby("category", as_index=False)["inventory_value"]
    .sum()
    .sort_values("inventory_value", ascending=False)
)

fig_inventory = px.bar(
    category_inventory,
    x="category",
    y="inventory_value",
    title="Inventory Value by Category",
    labels={
        "category": "Product Category",
        "inventory_value": "Inventory Value"
    },
    text_auto=".2s"
)

fig_inventory.update_layout(
    xaxis_tickangle=-45,
    xaxis_title="Product Category",
    yaxis_title="Inventory Value",
    margin=dict(l=20, r=20, t=60, b=100),
    height=500
)

# Product availability - Stacked Bar Chart
stock_summary = (
    filtered_df.groupby(["category", "availabilityStatus"])
    .size()
    .reset_index(name="product_count")
)

fig_stock = px.bar(
    stock_summary,
    x="category",
    y="product_count",
    color="availabilityStatus",
    title="Product Availability by Category",
    labels={
        "category": "Product Category",
        "product_count": "Number of Products",
        "availabilityStatus": "Availability Status"
    },
    barmode="stack"
)

fig_stock.update_layout(
    xaxis_tickangle=-45,
    xaxis_title="Product Category",
    yaxis_title="Number of Products",
    margin=dict(l=20, r=20, t=60, b=100),
    height=500,
    legend_title_text="Availability Status"
)

# Display charts side by side
chart1, chart2 = st.columns(2)

with chart1:
    st.plotly_chart(fig_inventory, use_container_width=True)

with chart2:
    st.plotly_chart(fig_stock, use_container_width=True)

# Product details
st.subheader("Product Details")

search_text = st.text_input("Search by product title or brand")

if search_text:
    mask = (
        filtered_df["title"].fillna("").str.contains(
            search_text, case=False, regex=False
        )
        | filtered_df["brand"].fillna("").str.contains(
            search_text, case=False, regex=False
        )
    )
    display_df = filtered_df[mask]
else:
    display_df = filtered_df

display_columns = [
    "title",
    "brand",
    "category",
    "price",
    "rating",
    "stock",
    "availabilityStatus",
    "inventory_value"
]

st.dataframe(
    display_df[display_columns],
    use_container_width=True,
    hide_index=True
)

st.caption("Data source: project SQLite products table.")