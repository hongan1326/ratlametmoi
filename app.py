import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
file_path = 'C:/Users/auqua/Documents/Billionaires Statistics Dataset.csv'  # chỉnh lại đường dẫn nếu cần
df = pd.read_csv(file_path)

# Nhóm dữ liệu theo 'Industry' và 'SelfMade'
industry_counts = df.groupby(['Industry', 'SelfMade'])['Name'].count().reset_index()

# Tạo lollipop chart
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

# Hiển thị trong Streamlit
st.pyplot(fig)

