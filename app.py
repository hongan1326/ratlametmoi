import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Billionaires Statistics - Interactive Lollipop Chart")

# Đọc dữ liệu từ file CSV trong repo
file_path = 'Billionaires Statistics Dataset.csv'  # Đảm bảo file nằm trong cùng thư mục với app.py
df = pd.read_csv(file_path)

# Kiểm tra tên cột (in ra cột để chắc chắn)
st.write(df.columns)

# Nhóm dữ liệu theo 'industries' và 'selfMade'
industry_counts = df.groupby(['industries', 'selfMade'])['personName'].count().reset_index()

# Tạo biểu đồ lollipop
fig = go.Figure()

# Thêm các đường thẳng cho biểu đồ lollipop
for industry in industry_counts['industries'].unique():
    sub_df = industry_counts[industry_counts['industries'] == industry]
    for _, row in sub_df.iterrows():
        fig.add_trace(go.Scatter(
            x=[row['industries'], row['industries']], 
            y=[0, row['personName']], 
            mode='lines+markers',
            marker=dict(color='green' if row['selfMade'] else 'blue', size=10),
            line=dict(color='black', width=2),
            name=f"{row['industries']} - {'Self Made' if row['selfMade'] else 'Not Self Made'}"
        ))

# Thiết lập tiêu đề và ghi chú cho biểu đồ
fig.update_layout(
    title='Interactive Lollipop Chart: Billionaires by Industry and Self Made Status',
    xaxis_title='Industry',
    yaxis_title='Number of Billionaires',
    xaxis=dict(tickmode='array', tickvals=industry_counts['industries'].unique(), tickangle=45),
    plot_bgcolor='white',  # Màu nền trắng
    paper_bgcolor='white',  # Màu nền giấy trắng
    font=dict(family='Arial', size=12, color='black'),
    margin=dict(l=0, r=0, b=50, t=40),
    showlegend=False
)

# Hiển thị biểu đồ trong Streamlit
st.plotly_chart(fig)
