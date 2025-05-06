import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Billionaires Statistics - Interactive 3D Chart")

# Đọc dữ liệu từ file CSV trong repo
file_path = 'Billionaires Statistics Dataset.csv'  # Đảm bảo file nằm trong cùng thư mục với app.py
df = pd.read_csv(file_path)

# Kiểm tra tên cột (in ra cột để chắc chắn)
st.write(df.columns)

# Nhóm dữ liệu theo 'industries' và 'selfMade'
industry_counts = df.groupby(['industries', 'selfMade'])['personName'].count().reset_index()

# Tạo biểu đồ 3D
fig = px.scatter(industry_counts, 
                 x='industries', 
                 y='selfMade', 
                 size='personName',  # Kích thước các cục tròn theo số lượng tỷ phú
                 color='selfMade',  # Màu sắc phân biệt tự lập và không tự lập
                 labels={'industries': 'Industry', 
                         'selfMade': 'Self Made', 
                         'personName': 'Number of Billionaires'},
                 color_continuous_scale=['blue', 'green'], 
                 title="Interactive 3D Chart: Billionaires by Industry and Self Made Status")

# Cập nhật cấu hình để tạo chiều sâu cho cục tròn
fig.update_traces(marker=dict(sizemode='diameter', 
                              opacity=0.7, 
                              line=dict(width=0.5, color='black')),
                  selector=dict(mode='markers'))

# Thiết lập tiêu đề và bố cục
fig.update_layout(
    title='Billionaires by Industry and Self Made Status',
    scene=dict(
        xaxis_title='Industry',
        yaxis_title='Self Made',
        zaxis_title='Number of Billionaires'
    ),
    margin=dict(l=0, r=0, b=0, t=40),  # Giảm không gian margin để biểu đồ rộng hơn
)

# Hiển thị biểu đồ trong Streamlit
st.plotly_chart(fig)
