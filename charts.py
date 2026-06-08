import streamlit as st
import plotly.express as px

def plot_salary_histogram(filtered_df):
    st.subheader("💰 Salary Distribution (Histogram)")
    fig = px.histogram(
        filtered_df, 
        x="Median", 
        nbins=20, 
        title="Distribution of Median Earnings",
        color_discrete_sequence=['#1f77b4'],
        marginal="box", # Adds a neat box plot on top!
        hover_data=['Major']
    )
    fig.update_layout(xaxis_title="Median Salary ($)", yaxis_title="Number of Majors")
    st.plotly_chart(fig, use_container_width=True)

def plot_unemployment_violin(filtered_df):
    st.subheader("🛡️ Job Security Density (Violin Plot)")
    fig = px.violin(
        filtered_df, 
        y="Unemployment_rate", 
        box=True, 
        points="all", 
        title="Density of Unemployment Rates",
        color_discrete_sequence=['#2ca02c'],
        hover_data=['Major']
    )
    fig.update_layout(yaxis_title="Unemployment Rate", xaxis_title="")
    fig.layout.yaxis.tickformat = ',.1%'
    st.plotly_chart(fig, use_container_width=True)

def plot_gender_boxplot(filtered_df):
    st.subheader("👩‍🎓 Demographic Spread (Box Plot)")
    fig = px.box(
        filtered_df, 
        y="ShareWomen", 
        points="all",
        title="Quartiles & Outliers: Share of Women",
        color_discrete_sequence=['#9467bd'],
        hover_data=['Major']
    )
    fig.update_layout(yaxis_title="Percentage of Women", xaxis_title="")
    fig.layout.yaxis.tickformat = ',.0%'
    st.plotly_chart(fig, use_container_width=True)

def plot_density_heatmap(filtered_df):
    st.subheader("🔥 Earnings vs Security (Density Heatmap)")
    fig = px.density_heatmap(
        filtered_df, 
        x="Unemployment_rate", 
        y="Median", 
        marginal_x="histogram", 
        marginal_y="histogram",
        title="Heatmap: Concentration of Majors",
        hover_data=['Major']
    )
    fig.update_layout(xaxis_title="Unemployment Rate", yaxis_title="Median Salary ($)")
    fig.layout.xaxis.tickformat = ',.1%'
    st.plotly_chart(fig, use_container_width=True)
