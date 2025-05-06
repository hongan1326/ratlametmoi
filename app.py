import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Billionaires Statistics - Interactive Lollipop Chart")

# Đọc dữ liệu từ file CSV
file_path = 'Billionaires Statistics Dataset.csv'
df = pd.read_csv(file_path)

# Lọc dữ liệu theo selfMade thông qua selectbox
self_made_options = df['selfMade'].dropna().unique().tolist()
selected_self_made = st.selectbox("Select Self-Made Status", options=self_made_options)

# Lọc dữ liệu theo lựa chọn
filtered_df = df[df['selfMade'] == selected_self_made]

# Nhóm theo industries
industry_counts = filtered_df.groupby('industries')['personName'].agg(['count', lambda names: ', '.join(names)]).reset_index()
industry_counts.columns = ['industries', 'count', 'names']

# Sắp xếp để hiển thị đẹp hơn
industry_counts = industry_counts.sort_values(by='count', ascending=True)

# Tạo biểu đồ lollipop
fig = go.Figure()

for _, row in industry_counts.iterrows():
    # Đường dọc
    fig.add_trace(go.Scatter(
        x=[0, row['count']],
        y=[row['industries'], row['industries']],
        mode='lines',
        line=dict(color='gray', width=1),
        showlegend=False
    ))

    # Marker đầu lollipop
    fig.add_trace(go.Scatter(
        x=[row['count']],
        y=[row['industries']],
        mode='markers',
        marker=dict(color='green' if selected_self_made else 'blue', size=10),
        text=f"{row['count']} Billionaires<br>{row['names']}",
        hoverinfo='text',
        showlegend=False
    ))

# Thiết lập layout
fig.update_layout(
    title='Lollipop Chart: Number of Billionaires by Industry',
    xaxis_title='Number of Billionaires',
    yaxis_title='Industry',
    plot_bgcolor='white',
    paper_bgcolor='white',
    xaxis=dict(showgrid=True, gridcolor='lightgray'),
    yaxis=dict(showgrid=False),
    font=dict(family='Arial', size=12, color='black'),
    margin=dict(l=50, r=50, b=50, t=50)
)

# Hiển thị biểu đồ
st.plotly_chart(fig)
