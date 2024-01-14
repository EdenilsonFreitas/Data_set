import streamlit as st
import pandas as pd 
import plotly.express as px

#st.set_page_config(title="Análise de preços de Combustível")
st.set_page_config(layout="wide")
df = pd.read_csv("preco_gasolina.csv", sep=";" , decimal=",")
df
#df["Date"] = pd.to_datetime(df["Date"])
#df=df.sort_values(df["Date"])

