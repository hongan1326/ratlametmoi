import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Billionaires Statistics - Interactive Chart")

# Đọc dữ liệu từ file CSV trong repo
file_path = 'Billionaires Statistics Dataset.csv'  # Đảm bảo file nằm trong cùng thư mục với app.py
df = pd.read_csv(file_path)

# Kiểm tra tên cột (in ra cột để chắc chắn)
st.write(df.columns)

# Nhóm dữ liệu theo 'industries' và 'selfMade'
industry_counts = df.groupby(['industries', 'selfMade'])['personName'].count().reset_index()

# Tạo biểu đồ Scatter với cục tròn có hiệu ứng chiều sâu
fig = px.scatter(industry_counts, 
                 x='industries', 
                 y='selfMade', 
                 size='personName',  # Kích thước cục tròn theo số lượng tỷ phú
                 color='selfMade',  # Màu sắc phân biệt tự lập và không tự lập
                 labels={'industries': 'Industry', 
                         'selfMade': 'Self Made', 
                         'personName': 'Number of Billionaires'},
                 color_continuous_scale=['blue', 'green'], 
                 title="Billionaires by Industry and Self Made Status")

# Cập nhật kiểu cho các cục tròn đẹp mắt hơn
fig.update_traces(marker=dict(sizemode='diameter', 
                              opacity=0.7, 
                              line=dict(width=1, color='black'),
                              symbol='circle'),
                  selector=dict(mode='markers'))

# Điều chỉnh layout để đẹp và dễ nhìn hơn
fig.update_layout(
    title='Billionaires by Industry and Self Made Status',
    xaxis_title='Industry',
    yaxis_title='Self Made Status',
    margin=dict(l=0, r=0, b=40, t=40),  # Đảm bảo có đủ không gian xung quanh biểu đồ
    plot_bgcolor='white',  # Màu nền trắng
    paper_bgcolor='white',  # Màu nền giấy trắng
    font=dict(family='Arial', size=12, color='black')
)

# Hiển thị biểu đồ trong Streamlit
st.plotly_chart(fig)
