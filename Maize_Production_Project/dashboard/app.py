

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Zambia Maize Production Dashboard")
st.write("This dashboard analyses maize production in selected districts.")

data = {
    "District": ["Lusaka", "Chongwe", "Kabwe", "Chipata", "Mumbwa"],
    "Production": [500, 350, 450, 600, 400],
}

df = pd.DataFrame(data)

st.subheader("Maize Production Data")
st.dataframe(df)

st.subheader("Production Statistics")

total = df["Production"].sum()
average = df["Production"].mean()

col1, col2 = st.columns(2)

col1.metric("Total Production", f"{total} tonnes")
col2.metric("Average Production", f"{average:.0f} tonnes")

st.subheader("Production by District")

fig, ax = plt.subplots()
ax.bar(df["District"], df["Production"])
ax.set_xlabel("District")
ax.set_ylabel("Production (tonnes)")
ax.set_title("Maize Production Comparison")
plt.xticks(rotation=30)

st.pyplot(fig)

st.subheader("Select a District")

selected_district = st.selectbox(
    "Choose a district:",
    df["District"]
)

result = df[df["District"] == selected_district]

st.write("Selected District:", selected_district)
st.write("Maize Production:", result["Production"].iloc[0], "tonnes")