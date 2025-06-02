import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns
from ui import *
import plotly.express as px 
import numpy as np

def show_the_reaper_has_a_soft_spot_for_men():    
    section_title("The Reaper Has a Soft Spot for Men!")
    section_description("It appears that men often enjoy the privilege of being portrayed as the central figure or <span class='red'>'killer'</span> in the story. But does that truly make them fortunate? It doesn't seem so:")


    death_by_gender = pd.read_csv('data/gender_race_breakdown.csv')  # Replace with the correct path to your dataset
    death_by_gender = death_by_gender[death_by_gender["Year"] >= 1980]
    death_by_gender = death_by_gender[["Year", "Male Cast", "Male Death", "Female Cast", "Female Death"]]
    death_by_gender = death_by_gender[death_by_gender["Male Death"] <= death_by_gender["Male Cast"]]
    death_by_gender = death_by_gender[death_by_gender["Female Death"] <= death_by_gender["Female Cast"]]

    # Calculate death rates for male and female characters
    male_data = pd.DataFrame({
        "Gender": "Male",
        "Death Count": death_by_gender["Male Death"] / death_by_gender["Male Cast"]
    })

    female_data = pd.DataFrame({
        "Gender": "Female",
        "Death Count": death_by_gender["Female Death"] / death_by_gender["Female Cast"]
    })

    death_by_gender = pd.concat([male_data, female_data], ignore_index=True)
    death_by_gender.replace([np.inf, -np.inf], np.nan, inplace=True)
    death_by_gender.dropna(subset=["Death Count"], how="all", inplace=True)
    death_by_gender = death_by_gender.groupby(by="Gender").mean().reset_index()
    death_by_gender["Death Count"] = death_by_gender["Death Count"].round(2)  # Round the death count values
    # Create a bar plot for death rates by gender
    fig_death = px.bar(
        death_by_gender,
        x="Gender",
        y="Death Count",
        text="Death Count",
        color="Gender",
        color_discrete_map={"Male": "#767171", "Female": "#FF1D1D"},
        title="10% Closer to the Edge: Men’s Higher Mortality Risk",
        labels={"Death Count": "Death Rate (%)"}
    )

    fig_death.update_layout(
        title=dict(text="10% Closer to the Edge: Men’s Higher Mortality Risk", x=0.2, font=dict(size=16, color="white")),
        xaxis_title_font=dict(size=14, color="white"),
        yaxis_title_font=dict(size=14, color="white"),
        font=dict(color="white"),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis_tickformat=".1%"
    )

    # Show the bar plot in Streamlit
    st.plotly_chart(fig_death)

    with st.expander("📊 Detailed Statistics for Death Rates by Gender", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### ⚰️ Death Rates")
            for _, row in death_by_gender.iterrows():
                st.metric(
                    f"{row['Gender']} Characters",
                    f"{row['Death Count']:.1%}",
                    "Rate of mortality in cast"
                )

        with col2:
            st.markdown("### 📈 Key Insights")
            male_death_rate = death_by_gender.loc[death_by_gender['Gender'] == 'Male', 'Death Count'].values[0]
            female_death_rate = death_by_gender.loc[death_by_gender['Gender'] == 'Female', 'Death Count'].values[0]
            st.markdown(f"""
            - **Higher death rate:** {'Male' if male_death_rate > female_death_rate else 'Female'} characters
            - **Death rate difference:** {abs(male_death_rate - female_death_rate):.2%}
            - **Overall average death rate:** {(death_by_gender['Death Count'].mean()):.2%}
            """)
    
    section_description(
        """
        This statistic speaks directly to the <span class='red'>Final Girl</span> trope, where the final survivor is often a woman. The
        trope highlights women as the emotional backbone of the story, symbolizing purity, endurance,
        and resilience, while men take the fall, often to serve a narrative purpose.
        """)
    
    col1, col2, col3= st.columns(3)

    # Add images to each column
    with col1:
        st.image("static/texas_chainsaw.jpg")
        st.markdown("<p style='text-align: center;'>Texas Chainsaw Massacre (1974)", unsafe_allow_html=True)

    with col2:
        st.image("static/scream.jpg")
        st.markdown("<p style='text-align: center;'>Scream (2000)", unsafe_allow_html=True)

    with col3:
        st.image("static/wrong_turn.jpg")
        st.markdown("<p style='text-align: center;'>Wrong Turn (2021)", unsafe_allow_html=True)
