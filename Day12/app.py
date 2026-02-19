import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("Sales Analytics Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("sales_data.csv")

df = load_data()

df.drop_duplicates(inplace=True)

df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")

df["Sales"].fillna(df["Sales"].mean(), inplace=True)
df["Profit"].fillna(0, inplace=True)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df = df[df["Sales"] > 0]

st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

payment = st.sidebar.multiselect(
    "Select Payment Mode",
    df["Payment_Mode"].unique(),
    default=df["Payment_Mode"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Payment_Mode"].isin(payment))
]

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order_ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹ {total_sales:,.0f}")
col2.metric("Total Profit", f"₹ {total_profit:,.0f}")
col3.metric("Total Orders", total_orders)

st.markdown("---")

st.subheader("Sales Trend")

sales_trend = filtered_df.groupby("Order_Date")["Sales"].sum()

fig1, ax1 = plt.subplots()
ax1.plot(sales_trend.index, sales_trend.values)
ax1.set_xlabel("Date")
ax1.set_ylabel("Sales")
st.pyplot(fig1)

st.subheader("Sales by Category")

category_sales = filtered_df.groupby("Category")["Sales"].sum()

fig2, ax2 = plt.subplots()
ax2.bar(category_sales.index, category_sales.values)
ax2.set_xlabel("Category")
ax2.set_ylabel("Sales")
st.pyplot(fig2)

st.subheader("Profit Distribution")

fig3, ax3 = plt.subplots()
sns.histplot(filtered_df["Profit"], kde=True, ax=ax3)
st.pyplot(fig3)

st.subheader("Correlation Heatmap")

fig4, ax4 = plt.subplots()
sns.heatmap(filtered_df.corr(numeric_only=True), annot=True, ax=ax4)
st.pyplot(fig4)

st.subheader("Filtered Data Preview")
st.dataframe(filtered_df)

st.success("Dashboard Loaded Successfully")
