import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Billionaires Statistics - Interactive Lollipop Chart")

# Đọc dữ liệu từ file CSV trong repo
file_path = 'Billionaires Statistics Dataset.csv'  # Đảm bảo file nằm trong cùng thư mục với app.py
df = pd.read_csv(file_path)

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
            mode='lines+markers+text',  # Thêm văn bản (ghi chú)
            marker=dict(color='green' if row['selfMade'] else 'blue', size=10),
            line=dict(color='gray', width=1),  # Đổi đường line thành màu xám nhạt
            text=f"{row['personName']}",  # Hiển thị số lượng người
            textposition="top center",  # Vị trí ghi chú trên mỗi cục
            textfont=dict(family='Arial', size=14, color='#000000')  # Màu chữ ghi chú là đen tuyền + size lớn hơn
        ))

# Thiết lập tiêu đề và ghi chú cho biểu đồ
fig.update_layout(
    title={'text': 'Interactive Lollipop Chart: Billionaires by Industry and Self Made Status', 
           'font': {'size': 22, 'family': 'Arial', 'color': '#000000', 'bold': True}},  # Tiêu đề in đậm và màu đen tuyền
    xaxis_title='Industry',
    yaxis_title='Number of Billionaires',
    xaxis=dict(
        tickmode='array', 
        tickvals=industry_counts['industries'].unique(), 
        tickangle=45,
        title_font=dict(family='Arial', size=16, color='#000000'),  # Màu chữ trục X đen tuyền + to hơn
        tickfont=dict(family='Arial', size=12, color='#000000')     # Tick text màu đen
    ),
    yaxis=dict(
        showgrid=True, 
        gridcolor='lightgray', 
        title_font=dict(family='Arial', size=16, color='#000000'),  # Màu chữ trục Y đen tuyền + to hơn
        tickfont=dict(family='Arial', size=12, color='#000000')     # Tick text màu đen
    ),
    plot_bgcolor='white',  # Màu nền trắng
    paper_bgcolor='white',  # Màu nền giấy trắng
    font=dict(family='Arial', size=13, color='#000000'),  # Màu chữ chung là đen tuyền
    margin=dict(l=0, r=0, b=50, t=50),
    showlegend=False
)

# Hiển thị biểu đồ trong Streamlit
st.plotly_chart(fig)
