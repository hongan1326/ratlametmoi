import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Billionaires Statistics - 3D Lollipop Chart")

# Đọc dữ liệu từ file CSV trong repo
file_path = 'Billionaires Statistics Dataset.csv'  # Đảm bảo file nằm trong cùng thư mục với app.py
df = pd.read_csv(file_path)

# Kiểm tra tên cột (in ra cột để chắc chắn)
st.write(df.columns)

# Nhóm dữ liệu theo 'industries' và 'selfMade'
industry_counts = df.groupby(['industries', 'selfMade'])['personName'].count().reset_index()

# Tạo biểu đồ 3D với Plotly
fig = px.scatter_3d(industry_counts, 
                    x='industries', 
                    y='selfMade', 
                    z='personName', 
                    color='selfMade', 
                    labels={'industries': 'Industry', 
                            'selfMade': 'Self Made', 
                            'personName': 'Number of Billionaires'},
                    color_continuous_scale=['blue', 'green'])

fig.update_traces(marker=dict(size=10))

# Thiết lập tiêu đề và ghi chú
fig.update_layout(
    title='3D Lollipop Chart: Number of Billionaires by Industry and Self Made Status',
    scene=dict(
        xaxis_title='Industry',
        yaxis_title='Self Made',
        zaxis_title='Number of Billionaires'
    )
)

# Hiển thị biểu đồ trong Streamlit
st.plotly_chart(fig)
