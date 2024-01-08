import streamlit as st
import pandas as pd
Sustainability_df=pd.read_csv("WorldSustainabilityDataset.csv")


richest=Sustainability_df.loc[Sustainability_df['Country Name'].isin(['Luxembourg','Macao SAR, China','Switzerland','Norway','Ireland','Iceland','Singapore','Qatar','United States','Denmark'])]
chart_data=richest.pivot(index='Year', columns='Country Name', values='Renewable energy consumption (% of total final energy consumption) - EG.FEC.RNEW.ZS')
#print(chart_data.tail())
st.title('Change in Renewable energy consumption over time for 10 countries with highest GDP per capita')
st.line_chart(chart_data)
st.write('World Sustainablity Dataset from:')
st.write('https://www.kaggle.com/datasets/truecue/worldsustainabilitydataset?resource=download')
st.header('By Asher Long')