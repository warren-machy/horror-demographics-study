from ui import *
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import streamlit_extras
from streamlit_extras.stylable_container import stylable_container
import numpy as np
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def show_a_new_dawn_for_hollywood():
    section_title("A New Dawn for Hollywood – The Rise of Female and Non-White Protagonists")
    @st.cache_data
    def load_protagonist_trends():
        # Read data with comma separator
        df = pd.read_csv('data/gender_race_breakdown.csv')

        # Convert Year to numeric and filter for years >= 1980
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        df = df[df['Year'] >= 1980]

        # Create 5-year periods for smoother visualization
        df['Period'] = ((df['Year'] // 5) * 5).astype(str) + '-' + ((df['Year'] // 5) * 5 + 4).astype(str)

        # Calculate stats by period for gender
        gender_stats = df.groupby('Period').agg({
            'Male Protagonists': 'sum',
            'Female Protagonists': 'sum',
            'Movie': 'count'
        }).reset_index()

        # Calculate proportions relative to total movies in period
        gender_stats['Male Ratio'] = gender_stats['Male Protagonists'] / gender_stats['Movie']
        gender_stats['Female Ratio'] = gender_stats['Female Protagonists'] / gender_stats['Movie']

        # Calculate stats by period for race
        race_stats = df.groupby('Period').agg({
            'Black Protagonists': 'sum',
            'Asian Protagonists': 'sum',
            'Male Protagonists': 'sum',
            'Female Protagonists': 'sum',
            'Movie': 'count'
        }).reset_index()

        # Calculate White and Non-White protagonists
        race_stats['White Protagonists'] = (race_stats['Male Protagonists'] + race_stats['Female Protagonists'] -
                                            race_stats['Black Protagonists'] - race_stats['Asian Protagonists'])
        race_stats['Non-White Protagonists'] = race_stats['Black Protagonists'] + race_stats['Asian Protagonists']

        # Calculate ratios
        race_stats['White Ratio'] = race_stats['White Protagonists'] / race_stats['Movie']
        race_stats['Non-White Ratio'] = race_stats['Non-White Protagonists'] / race_stats['Movie']

        return gender_stats, race_stats


    # Load the data
    gender_stats, race_stats = load_protagonist_trends()

    # Create subplots
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=("Protagonists by Gender", "Protagonists by Race"),
                        shared_yaxes=False,
                        horizontal_spacing=0.12,  # Slightly reduced spacing
                        column_widths=[0.5, 0.5])

    # Add gender trends
    fig.add_trace(
        go.Scatter(x=gender_stats['Period'], y=gender_stats['Male Ratio'],
                name='Male', line=dict(color='#808080', width=2)),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=gender_stats['Period'], y=gender_stats['Female Ratio'],
                name='Female', line=dict(color='#FF0000', width=2)),
        row=1, col=1
    )

    # Add race trends
    fig.add_trace(
        go.Scatter(x=race_stats['Period'], y=race_stats['White Ratio'],
                name='White', line=dict(color='#808080', width=2), showlegend=False),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=race_stats['Period'], y=race_stats['Non-White Ratio'],
                name='Non-White', line=dict(color='#FF0000', width=2), showlegend=False),
        row=1, col=2
    )

    # Update layout
    fig.update_layout(
        title=dict(
            text="",
            font=dict(size=24),
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top'
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=500,  # Reduced height for better proportion
        width=1300,  # Slightly increased width
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.95,
            xanchor="left",
            x=0.02,
            bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        ),
        margin=dict(t=100, l=60, r=60, b=60)  # Adjusted margins for better proportions
    )

    # Update axes
    fig.update_xaxes(showgrid=True, gridcolor='rgba(128,128,128,0.2)',
                    title_text="Time Period", title_font=dict(size=14),
                    zeroline=False, showline=True, linewidth=1, linecolor='white')
    fig.update_yaxes(showgrid=True, gridcolor='rgba(128,128,128,0.2)',
                    zeroline=False, showline=True, linewidth=1, linecolor='white',
                    title_font=dict(size=14),
                    title_text="Average Protagonists per Movie")

    # Set y-axis ranges
    fig.update_yaxes(range=[0, 3.5], row=1, col=1)
    fig.update_yaxes(range=[0, 3.5], row=1, col=2)

    # Update subplot titles style
    fig.update_annotations(font=dict(color='white', size=14))

    # Display the plot
    st.plotly_chart(fig)

    # Add caption
    st.caption("""Note: Values show the average number of protagonists per movie for each 5-year period. 
    Numbers can exceed 1.0 as movies may have multiple protagonists.""")

    # Add analysis metrics
    with st.expander("📊 Detailed Analysis", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 📈 Gender Trends")
            total_male = gender_stats['Male Protagonists'].sum()
            total_female = gender_stats['Female Protagonists'].sum()
            total_movies = gender_stats['Movie'].sum()
            st.metric("Overall Male-to-Female Ratio",
                    f"{(total_male / total_female):.2f}",
                    f"Based on {total_movies} movies from 1980 onwards")

        with col2:
            st.markdown("### 📈 Race Trends")
            total_white = race_stats['White Protagonists'].sum()
            total_nonwhite = race_stats['Non-White Protagonists'].sum()
            st.metric("Overall White-to-Non-White Ratio",
                    f"{(total_white / total_nonwhite):.2f}",
                    f"Based on {total_movies} movies from 1980 onwards")

    section_description(
        """
            Hollywood is witnessing a transformative era, where <span class='red'>female</span> and <span class='red'>non-white</span> protagonists and antagonists take center stage, 
            redefining the landscape of storytelling. These films highlight groundbreaking achievements in diverse representation,
             both in front of and behind the camera, showcasing the power of inclusivity and fresh perspectives in shaping modern <span class='red'>horror film industry</span>.
            """)

    col1, col2, col3, col4 = st.columns(4)

    # Add images to each column
    with col1:
        st.image("static/maxxine.jpg")
        st.markdown("<p style='text-align: center;'><b>MaXXXine (2024)</b><br>Best Independent Film of 2024</p>", unsafe_allow_html=True)

    with col2:
        st.image("static/ma.jpg")
        st.markdown("<p style='text-align: center;'><b>Ma (2019)</b><br>Best Horror Movie of 2019</p>", unsafe_allow_html=True)

    with col3:
        st.image("static/get_out.jpg")
        st.markdown("<p style='text-align: center;'><b>Get Out (2017)</b><br>FIRST African American director to get Best Original Screenplay</p>", unsafe_allow_html=True)

    with col4:
        st.image("static/us.jpg")
        st.markdown("<p style='text-align: center;'><b>Us (2019)</b><br>Best Writing</p>", unsafe_allow_html=True)
    # Villain Gender Distribution as Horizontal Stacked Bars
