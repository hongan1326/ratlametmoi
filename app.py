import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Billionaires Statistics - Lollipop Chart")

# Upload CSV file
uploaded_file = st.file_uploader("Billionaires Statistics Dataset, type=["csv"])

if uploaded_file is not None:
    # Read the CSV
    df = pd.read_csv(uploaded_file)

    # Group data by 'Industry' and 'SelfMade'
    industry_counts = df.groupby(['Industry', 'SelfMade'])['Name'].count().reset_index()

    # Create lollipop chart
    fig, ax = plt.subplots(figsize=(10, 6))

    industries = industry_counts['Industry'].unique()
    colors = {'True': 'green', 'False': 'blue'}

    for industry in industries:
        sub_df = industry_counts[industry_counts['Industry'] == industry]
        for _, row in sub_df.iterrows():
            ax.plot([industry, industry], [0, row['Name']],
                    marker='o',
                    color=colors[str(row['SelfMade'])])

    ax.set_xlabel('Industry')
    ax.set_ylabel('Number of Billionaires')
    ax.set_title('Lollipop Chart: Number of Billionaires by Industry and SelfMade Status')
    plt.xticks(rotation=90)

    # Show chart in Streamlit
    st.pyplot(fig)
else:
    st.info("Please upload a CSV file to see the chart.")
