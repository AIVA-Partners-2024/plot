import plotly.express as px
import streamlit as st

data_frame = {'India': 4500,
              'Australia': 2500,
              'Japan': 1053,
              'America': 500,
              'Russia': 3200  }

fig = px.pie(
    hole = 0.2,
    labels = data_frame.values(),
    names = data_frame.keys(),
)

st.header("Donut chart")
st.plotly_chart(fig)