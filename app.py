import streamlit as st
from data import load_data
from filters import get_category_filters
from charts import plot_salary_histogram, plot_unemployment_violin, plot_gender_boxplot, plot_density_heatmap

st.set_page_config(page_title="College Majors Dashboard", layout="centered")

df = load_data()

st.title("🎓 US College Majors Dashboard")
st.markdown("Advanced statistical analysis of earnings, job security, and demographics across college majors.")

selected_category = get_category_filters(df)

if selected_category == "All Categories":
    filtered_df = df
    st.markdown("### Showing data for: **All Categories**")
else:
    filtered_df = df[df['Major_category'] == selected_category]
    st.markdown(f"### Showing data for: **{selected_category}**")

# Top Level Metrics
avg_salary = filtered_df['Median'].mean()
avg_unemployment = filtered_df['Unemployment_rate'].mean()

col1, col2 = st.columns(2)
col1.metric("Average Median Salary", f"${avg_salary:,.0f}")
col2.metric("Average Unemployment Rate", f"{avg_unemployment*100:.1f}%")

st.markdown("---")

plot_salary_histogram(filtered_df)
st.markdown("---")

plot_unemployment_violin(filtered_df)
st.markdown("---")

plot_gender_boxplot(filtered_df)
st.markdown("---")

plot_density_heatmap(filtered_df)

st.markdown("---")
st.markdown("Data Source: [FiveThirtyEight College Majors Dataset](https://github.com/fivethirtyeight/data/tree/master/college-majors)")
