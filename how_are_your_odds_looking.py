import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from ui import *

def show_how_are_your_odds_looking():
    section_title("How Are Your Odds Looking? 🎭")
    section_description("How would you fare if you were in a horror movie? Enter your demographics below and find out!")
    # st.caption("Explore the probabilities in your favorite horror settings.")

    col1, col2 = st.columns(2)
    data = pd.read_csv("data/gender_race_breakdown.csv")

    # Filter based on cast vs death numbers
    # filtered_data = data[
    #     (data['Male Cast'] > data['Male Death']) &
    #     (data['Female Cast'] > data['Female Death']) &
    #     (data['Black Cast'] > data['Black Death']) &
    #     (data['Asian Cast'] > data['Asian Death'])
    # ]

    with col1:
        st.markdown(
            """
            <h3 style="text-align: center;">Enter Your Data</h2>
            """,
            unsafe_allow_html=True,
        )
        time_span = st.slider(
            "Horror Movie Year Range", 
            1984, 2024, 
            (1984, 2024), 
            help="Choose the range of years for your analysis."
        )
        gender = st.selectbox("Select Gender", ["Female", "Male"])
        race = st.selectbox("Select Race", ["Asian", "Black", "White"])
        submit = st.button("Submit")

        if race == "White":
            filtered_data = data[
                (data['Male Cast'] > data['Male Death']) &
                (data['Female Cast'] > data['Female Death'])
            ]
        elif race == "Black":
            filtered_data = data[
                (data['Black Cast'] > data['Black Death']) &
                (data['Male Cast'] > data['Male Death']) &
                (data['Female Cast'] > data['Female Death'])
            ]
        elif race == "Asian":
            filtered_data = data[
                (data['Asian Cast'] > data['Asian Death']) &
                (data['Male Cast'] > data['Male Death']) &
                (data['Female Cast'] > data['Female Death'])
            ]
        else:
            filtered_data = data  # Default fallback if no specific race is selected
    with col2:
        st.markdown(
            """
            <h3 style="text-align: center;">Results</h2>
            """,
            unsafe_allow_html=True,
        )

        if not submit:
            st.markdown(
                """
                <div style="text-align: center; font-size: 18px;">Submit to check your statistics!</div>
                """,
                unsafe_allow_html=True
            )
        else:
            with st.spinner("Calculating, please wait..."):
                time.sleep(2)  # Simulate backend calculation delay

            # Filter dataset based on year range
            filtered_data = filtered_data[(filtered_data['Year'] >= time_span[0]) & (filtered_data['Year'] <= time_span[1])]

            if not filtered_data.empty:
                filtered_data['White Protagonists'] = (
                    filtered_data['Male Protagonists'] +
                    filtered_data['Female Protagonists'] -
                    filtered_data['Asian Protagonists'] -
                    filtered_data['Black Protagonists']
                )

                filtered_data['White Cast'] = (
                    filtered_data['Male Cast'] + filtered_data['Female Cast']
                )

                filtered_data['White Death'] = (
                    filtered_data['Male Death'] + filtered_data['Female Death']
                )

                # Debugging: Verify the calculations
                print("White Protagonists:\n", filtered_data['White Protagonists'].head())
                print("White Cast:\n", filtered_data['White Cast'].head())
                print("White Death:\n", filtered_data['White Death'].head())

                # Step 2: Determine relevant columns dynamically
                if race == "White":
                    protagonist_key = "White Protagonists"
                    cast_column = "White Cast"
                    death_column = "White Death"
                else:
                    protagonist_key = f"{race} Protagonists"
                    cast_column = f"{race} Cast"
                    death_column = f"{race} Death"

                # Debugging: Check if these columns exist and are populated
                if protagonist_key not in filtered_data.columns or cast_column not in filtered_data.columns or death_column not in filtered_data.columns:
                    raise ValueError(f"Required columns missing: {protagonist_key}, {cast_column}, {death_column}")

                # Step 3: Filter data for the selected gender and race
                gender_race_filtered = filtered_data[
                    (filtered_data[cast_column] > 0) &
                    (filtered_data[protagonist_key] > 0)
                ]

                # Debugging: Inspect the filtered data
                print("Filtered Data for Gender and Race:\n", gender_race_filtered.head())

                # Step 4: Calculate Protagonist Odds
                if gender_race_filtered[cast_column].sum() > 0:  # Avoid division by zero
                    protagonist_odds = (
                        gender_race_filtered[protagonist_key].sum() /
                        gender_race_filtered[cast_column].sum()
                    )
                else:
                    protagonist_odds = 0  # Handle case with no valid data

                # Debugging: Print intermediate values for odds calculation
                print("Protagonist Key Sum:", gender_race_filtered[protagonist_key].sum())
                print("Cast Column Sum:", gender_race_filtered[cast_column].sum())
                print("Protagonist Odds:", protagonist_odds)

                # Step 5: Calculate Death Odds
                if gender_race_filtered[cast_column].sum() > 0:  # Avoid division by zero
                    death_odds = (
                        gender_race_filtered[death_column].sum() /
                        gender_race_filtered[cast_column].sum()
                    )
                else:
                    death_odds = 0  # Handle case with no valid data

                villain_gender_race = gender_race_filtered[(gender_race_filtered['Gender Villain'] == gender)]
                if villain_gender_race[cast_column].sum() > 0:  # Avoid division by zero
                    villain_odds = (
                        villain_gender_race[death_column].sum() /
                        villain_gender_race[cast_column].sum()
                    )
                else:
                    villain_odds = 0  # Handle case with no valid data
                # # Villain odds
                # villain_gender_race = gender_race_filtered[(gender_race_filtered['Gender Villain'] == gender)]
                # villain_odds = len(villain_gender_race) / len(gender_race_filtered)

                # Race-specific villain odds
                # race_villain_odds = len(
                #     gender_race_filtered[
                #         (gender_race_filtered['Gender Villain'] == gender) &
                #         (gender_race_filtered['Villain Race'] == race)
                #     ]
                # ) / len(gender_race_filtered)

                # Display progress bars with a fade-in effect
                # Villain Progress
                progress_bar = st.empty()
                caption = st.empty()
                for i in range(int(villain_odds * 100) + 1):
                    progress_bar.progress(i / 100)
                    caption.caption(f"🦹 Villain: {i}%")
                    time.sleep(0.01)

                # Killed Progress
                progress_bar = st.empty()
                caption = st.empty()
                for i in range(int(death_odds * 100) + 1):
                    progress_bar.progress(i / 100)
                    caption.caption(f"💀 Killed: {i}%")
                    time.sleep(0.01)

                # Protagonist Progress
                progress_bar = st.empty()
                caption = st.empty()
                for i in range(int(protagonist_odds * 100) + 1):
                    progress_bar.progress(i / 100)
                    caption.caption(f"🌟 Protagonist: {i}%")
                    time.sleep(0.01)

            else:
                st.write("No data available for the selected year range.")
