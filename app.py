import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Thống kê Tỷ phú - Biểu đồ Lollipop")

# Đọc dữ liệu từ file CSV trong repo
file_path = 'Billionaires Statistics Dataset.csv'  # Đảm bảo file nằm trong cùng thư mục với app.py
df = pd.read_csv(file_path)

# Kiểm tra tên cột (in ra cột để chắc chắn)
st.write(df.columns)

# Nhóm dữ liệu theo 'industries' và 'selfMade'
industry_counts = df.groupby(['industries', 'selfMade'])['Name'].count().reset_index()

# Tạo biểu đồ lollipop
fig, ax = plt.subplots(figsize=(10, 6))

industries = industry_counts['industries'].unique()
colors = {'True': 'green', 'False': 'blue'}

for industry in industries:
    sub_df = industry_counts[industry_counts['industries'] == industry]
    for _, row in sub_df.iterrows():
        ax.plot([industry, industry], [0, row['Name']],
                marker='o',
                color=colors[str(row['selfMade'])])

ax.set_xlabel('Ngành nghề')
ax.set_ylabel('Số lượng tỷ phú')
ax.set_title('Biểu đồ Lollipop: Số lượng tỷ phú theo ngành và tình trạng tự lập')
plt.xticks(rotation=90)

# Hiển thị biểu đồ trong Streamlit
st.pyplot(fig)
