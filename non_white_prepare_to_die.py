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

def show_non_white_prepare_to_die():
    section_title("Non White? Prepare to die!")
    
    @st.cache_data
    def calculate_death_rates():
        # Read data and filter for years >= 1980
        df = pd.read_csv('data/gender_race_breakdown.csv')
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        df = df[df['Year'] >= 1980].copy()

        # Create a copy for calculations exactly as in the image
        death_by_race = df.copy()

        # Select only the required columns exactly as in image
        death_by_race = death_by_race[["Black Cast", "Black Death", "Asian Cast", "Asian Death",
                                    "Male Cast", "Male Death", "Female Cast", "Female Death", "Year"]]

        # Calculate exactly as shown in the image
        death_by_race["White Cast"] = death_by_race["Male Cast"] + death_by_race["Female Cast"] - \
                                    death_by_race["Black Cast"] - death_by_race["Asian Cast"]

        death_by_race["White Death"] = death_by_race["Male Death"] + death_by_race["Female Death"] - \
                                    death_by_race["Black Death"] - death_by_race["Asian Death"]

        death_by_race["Non-White Cast"] = death_by_race["Black Cast"] + death_by_race["Asian Cast"]
        death_by_race["Non-White Death"] = death_by_race["Black Death"] + death_by_race["Black Death"]

        # Calculate death rates exactly as in image
        death_by_race = death_by_race[death_by_race["Non-White Death"] <= death_by_race["Non-White Cast"]]
        death_by_race = death_by_race[death_by_race["White Death"] <= death_by_race["White Cast"]]

        # Create white and non-white DataFrames exactly as in image
        white_data = pd.DataFrame({
            "Race": "White",
            "Death Count": death_by_race["White Death"] / death_by_race["White Cast"]
        })

        non_white_data = pd.DataFrame({
            "Race": "Non-White",
            "Death Count": death_by_race["Non-White Death"] / death_by_race["Non-White Cast"]
        })

        # Combine and process exactly as shown in the image
        death_by_race_final = pd.concat([white_data, non_white_data], ignore_index=True)
        death_by_race_final = death_by_race_final[death_by_race_final["Death Count"] > 0]
        death_by_race_final = death_by_race_final.groupby(by="Race").mean().reset_index()

        # Add total counts for the detailed statistics
        overall_stats = death_by_race_final.copy()
        overall_stats["Total Cast"] = [death_by_race["Non-White Cast"].sum(), death_by_race["White Cast"].sum()]
        overall_stats["Total Deaths"] = [death_by_race["Non-White Death"].sum(), death_by_race["White Death"].sum()]

        # Calculate decade-wise statistics for the trend analysis
        death_by_race['Decade'] = (death_by_race['Year'] // 10) * 10

        decade_stats = death_by_race.groupby('Decade').agg({
            'White Cast': 'sum',
            'White Death': 'sum',
            'Non-White Cast': 'sum',
            'Non-White Death': 'sum'
        }).reset_index()

        decade_stats['White Death Rate'] = (decade_stats['White Death'] / decade_stats['White Cast']).round(4) * 100
        decade_stats['Non-White Death Rate'] = (decade_stats['Non-White Death'] / decade_stats['Non-White Cast']).round(
            4) * 100

        return overall_stats, decade_stats


    # Calculate the data
    overall_stats, decade_stats = calculate_death_rates()

    # Create subplots with adjusted dimensions
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=("Overall Death Rates (1980-Present)", "Death Rate Trends by Decade"),
                        horizontal_spacing=0.12,
                        column_widths=[0.5, 0.5])

    # Add main death rate comparison
    fig.add_trace(
        go.Bar(x=overall_stats["Race"],
            y=overall_stats["Death Count"],
            text=overall_stats["Death Count"].apply(lambda x: f"{x:.1%}"),
            textposition='outside',
            marker_color=["#767171", "#FF1D1D"],
            name='Overall Death Rate',
            showlegend=False,
            hovertemplate="<b>%{x}</b><br>" +
                            "Death Rate: %{y:.1%}<br>" +
                            "<extra></extra>"),
        row=1, col=1
    )

    # Add decade trends
    fig.add_trace(
        go.Scatter(x=decade_stats['Decade'],
                y=decade_stats['White Death Rate'],
                name='White',
                line=dict(color='#767171', width=2),
                hovertemplate="<b>%{x}s</b><br>" +
                                "Death Rate: %{y:.1f}%<br>" +
                                "<extra></extra>"),
        row=1, col=2
    )

    fig.add_trace(
        go.Scatter(x=decade_stats['Decade'],
                y=decade_stats['Non-White Death Rate'],
                name='Non-White',
                line=dict(color='#FF1D1D', width=2),
                hovertemplate="<b>%{x}s</b><br>" +
                                "Death Rate: %{y:.1f}%<br>" +
                                "<extra></extra>"),
        row=1, col=2
    )

    # Update layout with new dimensions and styling
    fig.update_layout(
        title=dict(
            text="The Deadly Reality of Horror Movies",
            font=dict(size=24),
            y=0.95,
            x=0.5,
            xanchor='center',
            yanchor='top'
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=400,  # Ensure height matches width for square plots
        width=800,   # Set equal width and height for square layout
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.95,
            xanchor="left",
            x=0.55,
            bgcolor='rgba(0,0,0,0)',
            font=dict(color='white')
        ),
        margin=dict(t=100, l=60, r=60, b=60)
    )

    # Update axes
    fig.update_xaxes(showgrid=True,
                    gridcolor='rgba(128,128,128,0.2)',
                    zeroline=False,
                    showline=True,
                    linewidth=1,
                    linecolor='white')

    fig.update_yaxes(showgrid=True,
                    gridcolor='rgba(128,128,128,0.2)',
                    zeroline=False,
                    showline=True,
                    linewidth=1,
                    linecolor='white',
                    title_font=dict(size=14))

    # Update y-axis titles
    fig.update_yaxes(title_text="Death Rate (%)", row=1, col=1)
    fig.update_yaxes(title_text="Death Rate (%)", row=1, col=2)

    # Update subplot titles style
    fig.update_annotations(font=dict(color='white', size=14))

    # Display the plot
    st.plotly_chart(fig)

    # Add detailed statistics in an expander
    with st.expander("📊 Detailed Statistics", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 💀 Death Rates")
            for _, row in overall_stats.iterrows():
                st.metric(
                    f"{row['Race']} Characters",
                    f"{row['Death Count']:.1%}",
                    f"Total Cast: {row['Total Cast']:,}"
                )

        with col2:
            st.markdown("### 📈 Key Findings")
            death_rate_ratio = overall_stats.iloc[0]["Death Count"] / overall_stats.iloc[1]["Death Count"]
            st.markdown(f"""
            - Non-white characters are **{death_rate_ratio:.1f}x** more likely to die
            - Total deaths analyzed: **{overall_stats['Total Deaths'].sum():,}**
            - Highest death rate decade: **{decade_stats.iloc[decade_stats['Non-White Death Rate'].argmax()]['Decade']}s**
            """)

    # Add impactful caption
    # st.markdown("""
    # ---
    # **Analysis Impact**: This visualization reveals a stark reality in horror films - the significant disparity in survival rates 
    # between white and non-white characters. The trend analysis shows how this bias has evolved over decades, highlighting the need 
    # for more equitable representation in the genre.
    # """)

    section_description(
        """
            This statistic aligns with the <span class='red'>Magical Negro</span> trope, where black characters are often portrayed as
            wise, badass, spiritual guides who assist white protagonists, only to meet tragic ends. Their
            deaths are frequently used as plot devices to further the <span class='red'>hero's journey</span>, underscoring systemic
            racial biases in storytelling.
        """)
    
    col1, col2, col3= st.columns(3)

    # Add images to each column
    with col1:
        st.image("static/predator.jpg")
        st.markdown("<p style='text-align: center;'>Predator (1987)<br>Helps protagonist – dies.", unsafe_allow_html=True)

    with col2:
        st.image("static/predators.jpg")
        st.markdown("<p style='text-align: center;'>Predators (2010)<br>Helps protagonist – dies.", unsafe_allow_html=True)

    with col3:
        st.image("static/chucky.jpg")
        st.markdown("<p style='text-align: center;'>Chucky (1988)<br>Helps protagonist – dies.", unsafe_allow_html=True)
