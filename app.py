import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load data
df = pd.read_csv('Billionaires Statistics Dataset.csv')

# Group by industries and selfMade
count_df = df.groupby(['industries', 'selfMade']).size().reset_index(name='count')

# Streamlit app
st.title('Lollipop Chart: Number of Billionaires by Industry and Self-Made Status')

# Select selfMade filter
self_made_options = count_df['selfMade'].unique().tolist()
selected_self_made = st.selectbox('Select Self-Made Status:', self_made_options)

# Filter data
filtered_df = count_df[count_df['selfMade'] == selected_self_made]

# Sort for better visuals
filtered_df = filtered_df.sort_values('count', ascending=True)

# Plotly Lollipop chart
fig = go.Figure()

# Add stems
fig.add_trace(go.Scatter(
    x=filtered_df['count'],
    y=filtered_df['industries'],
    mode='lines',
    line=dict(color='gray', width=2),
    showlegend=False
))

# Add markers
fig.add_trace(go.Scatter(
    x=filtered_df['count'],
    y=filtered_df['industries'],
    mode='markers',
    marker=dict(color='blue', size=10),
    name='Billionaires'
))

fig.update_layout(
    xaxis_title='Number of Billionaires',
    yaxis_title='Industry',
    title=f'Lollipop Chart for Self-Made Status: {selected_self_made}',
    template='plotly_white',
    height=600
)

st.plotly_chart(fig)
