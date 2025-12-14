import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# interactive dashboard
# streamlit - build in 

# plotly 
# holoview
# hview
# folium

st.title("Dasboard Creation")
st.write("Sales Data Analysis")

df=pd.read_csv('supermarket_sales.csv')

print(df.head())
print(df.columns)

#------------------Side bar Data Entry----------------------------------

st.sidebar.header("Data Entry")
filtered_df=df.copy()

city=st.sidebar.selectbox("Select city",['All']+df.City.unique().tolist())
branch=st.sidebar.selectbox("Select Branch",['All']+df.Branch.unique().tolist())
cus_type=st.sidebar.selectbox("Select Customer Type",['All']+df['Customer type'].unique().tolist())
gender=st.sidebar.selectbox("Select gender",['All']+df.Gender.unique().tolist())

if city!='All':
    filtered_df=filtered_df[filtered_df.City==city]
if branch!='All':
    filtered_df=filtered_df[filtered_df.Branch==branch]
if cus_type!='All':
    filtered_df=filtered_df[filtered_df['Customer type']==cus_type]
if gender!='All':
    filtered_df=filtered_df[filtered_df.Gender==gender]

# Customer type
# Gender

#----------------Showing KPI data--------------
col1,col2,col3=st.columns(3)
col1.metric("Total sale ",f"${filtered_df['Total'].sum()}")
col2.metric("Average gross income ",f"${filtered_df['gross income'].mean()}")
col3.metric("Total quantity ",f"${filtered_df['Quantity'].sum()}")

#--------------Showing Tabel---------------------------
st.write(filtered_df)
print(filtered_df)
col1,col2=st.columns(2)
with col1:
    sales=filtered_df.groupby('City')['Total'].sum().reset_index()
    fig,ax=plt.subplots()
    ax.bar(x=sales['City'],height=sales['Total'])
    st.pyplot(fig)
    

with col2:
    import plotly.express as px  #pip install plotly
    sales=filtered_df.groupby('City')['Total'].sum().reset_index()
    fig = px.bar(
        sales,
        x='City',
        y='Total',
        title='Total Sales by City',
        labels={'Total': 'Total Sales', 'City': 'City'},
        text='Total'
    )
    st.plotly_chart(fig)
