import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Billionaires Statistics - Interactive Lollipop Chart")

# Load dữ liệu
file_path = 'Billionaires Statistics Dataset.csv'
df = pd.read_csv(file_path)

# Lọc Self-Made
self_made_options = df['selfMade'].dropna().unique().tolist()
selected_self_made = st.selectbox("Select Self-Made Status", options=self_made_options)

# Lọc theo lựa chọn
filtered_df = df[df['selfMade'] == selected_self_made]

# Nhóm theo ngành
industry_counts = filtered_df.groupby('industries')['personName'].agg(['count', lambda names: ', '.join(names)]).reset_index()
industry_counts.columns = ['industries', 'count', 'names']
industry_counts = industry_counts.sort_values(by='count', ascending=True)

# Vẽ lollipop chart
fig = go.Figure()

for _, row in industry_counts.iterrows():
    # Đường lollipop
    fig.add_trace(go.Scatter(
        x=[0, row['count']],
        y=[row['industries'], row['industries']],
        mode='lines',
        line=dict(color='gray', width=1),
        showlegend=False
    ))

    # Marker và hover
    fig.add_trace(go.Scatter(
        x=[row['count']],
        y=[row['industries']],
        mode='markers+text',
        marker=dict(color='green' if selected_self_made else 'blue', size=10),
        text=[str(row['count'])],
        textposition="middle right",
        textfont=dict(size=10, color='black'),  # Giảm cỡ chữ và đổi màu thành đen
        hovertemplate=f"<b>{row['industries']}</b><br>{row['count']} Billionaires<br>{row['names']}",
        name='Self Made' if selected_self_made else 'Not Self Made',
        showlegend=False  # tạm thời không lặp lại ở mỗi trace
    ))

# Thêm legend 1 lần duy nhất
fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='markers',
    marker=dict(color='green' if selected_self_made else 'blue', size=10),
    name='Self Made' if selected_self_made else 'Not Self Made'
))

# Layout
fig.update_layout(
    title='Lollipop Chart: Number of Billionaires by Industry',
    xaxis_title='Number of Billionaires',
    yaxis_title='Industry',
    plot_bgcolor='white',
    paper_bgcolor='white',
    xaxis=dict(showgrid=True, gridcolor='lightgray'),
    yaxis=dict(showgrid=False),
    font=dict(family='Arial', size=12, color='black'),
    margin=dict(l=50, r=50, b=50, t=50),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5)
)

# Hiển thị
st.plotly_chart(fig)
