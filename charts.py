import streamlit as st
import plotly.express as px
import pandas as pd

def plot_top_10_majors(filtered_df):
    st.subheader("💰 Top 10 Highest Paying Majors (Treemap)")
    top_10 = filtered_df.nlargest(10, 'Median')
    
    fig = px.treemap(
        top_10,
        path=[px.Constant("Majors"), 'Major'],
        values='Median',
        color='Median',
        color_continuous_scale='Blues',
    )
    fig.update_traces(textinfo="label+value", texttemplate="%{label}<br>$%{value:,.0f}")
    fig.update_layout(margin=dict(t=10, l=10, r=10, b=10))
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

def plot_gender_breakdown(filtered_df):
    st.subheader("👩‍🎓 Overall Gender Breakdown")
    total_men = filtered_df['Men'].sum()
    total_women = filtered_df['Women'].sum()
    
    gender_data = pd.DataFrame({
        'Gender': ['Men', 'Women'],
        'Total': [total_men, total_women]
    })
    
    fig = px.pie(
        gender_data,
        names='Gender',
        values='Total',
        hole=0.4,
        color='Gender',
        color_discrete_map={'Men': '#1f77b4', 'Women': '#e377c2'}
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)
