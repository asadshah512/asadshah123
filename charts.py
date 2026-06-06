import streamlit as st
import plotly.express as px

def plot_top_10_majors(filtered_df):
    st.subheader("💰 Top 10 Highest Paying Majors")
    top_10 = filtered_df.nlargest(10, 'Median').sort_values('Median', ascending=True)
    
    fig = px.bar(
        top_10, 
        x='Median', 
        y='Major', 
        orientation='h',
        text_auto='$.2s',
        color_discrete_sequence=['#1f77b4']
    )
    fig.update_layout(xaxis_title="Median Salary ($)", yaxis_title="", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

def plot_lowest_unemployment(filtered_df):
    st.subheader("🛡️ Top 10 Majors with Best Job Security (Lowest Unemployment)")
    top_10_secure = filtered_df.nsmallest(10, 'Unemployment_rate').sort_values('Unemployment_rate', ascending=False)
    
    fig = px.bar(
        top_10_secure, 
        x='Unemployment_rate', 
        y='Major', 
        orientation='h',
        text_auto='.1%',
        color_discrete_sequence=['#2ca02c']
    )
    fig.update_layout(xaxis_title="Unemployment Rate", yaxis_title="", showlegend=False)
    fig.layout.xaxis.tickformat = ',.0%'
    st.plotly_chart(fig, use_container_width=True)

def plot_highest_share_women(filtered_df):
    st.subheader("👩‍🎓 Top 10 Majors with Highest Percentage of Women")
    top_10_women = filtered_df.nlargest(10, 'ShareWomen').sort_values('ShareWomen', ascending=True)
    
    fig = px.bar(
        top_10_women, 
        x='ShareWomen', 
        y='Major', 
        orientation='h',
        text_auto='.1%',
        color_discrete_sequence=['#9467bd']
    )
    fig.update_layout(xaxis_title="Percentage of Women", yaxis_title="", showlegend=False)
    fig.layout.xaxis.tickformat = ',.0%'
    st.plotly_chart(fig, use_container_width=True)
