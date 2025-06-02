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

def show_villanous_landscape():
    # Page Title
    section_title("The Villanous Landscape", margin_top="5em")
    section_description(
        """
        But is Ann merely <span class='red'>imagining</span> things, or is there something more <span class='red'>sinister</span> behind the Grim Reaper’s choice of Hollywood’s villains?
         Let’s delve into the statistics and uncover the hidden truths lurking beneath the surface.""", margin_bottom="-4em",
    )

    # Set plot background to transparent
    plt.rcParams['figure.facecolor'] = 'none'
    plt.rcParams['axes.facecolor'] = 'none'

    # Set the color of the axis labels and ticks to white
    plt.rcParams['text.color'] = 'white'
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'

    plt.rcParams['font.size'] = 14  # Adjust font size as needed

    # Load data
    data = pd.read_csv('data/gender_race_breakdown.csv')

    villain_demo = data.groupby(['Gender Villain', 'Villain Race']).size().reset_index(name='Count')
    villain_demo = villain_demo[
        (villain_demo["Gender Villain"].isin(["Female", "Male"])) & 
        (villain_demo["Villain Race"].isin(["White", "Black", "Asian"]))
    ]

    # Create a pivot table for a heatmap-friendly format
    villain_demo_pivot = villain_demo.pivot(index='Villain Race', columns='Gender Villain', values='Count').fillna(0).reset_index()

    # Create the heatmap plot using Plotly
    fig = px.imshow(
        villain_demo_pivot.set_index('Villain Race'),
        text_auto=True,
        color_continuous_scale=["#3B3838", "#FF1D1D"],
        labels=dict(x="Gender", y="Race", color="Count"),
        title="Demographics of Blockbuster Villains"
    )

    fig.update_layout(
        title=dict(text="Demographics of Blockbuster Villains", x=0.17, font=dict(size=24, color="white")),
        xaxis_title_font=dict(size=14, color="white"),
        yaxis_title_font=dict(size=14, color="white"),
        font=dict(size=20,color="white"),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        # coloraxis_showscale=False,  # Disable the color bar
        coloraxis_colorbar=dict(
            thickness=15,  # Adjust the thickness of the color bar
            len=0.5,  # Adjust the length of the color bar
            x=0.7  # Position closer to the heatmap
        ),
        # autosize=False,
        # width=500,  # Increase width to make it chonkier
        # height=500   # Adjust height as needed
    )

    # Show the plot in Streamlit
    st.plotly_chart(fig)

    with st.expander("📊 Detailed Statistics", expanded=False):
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🎭 Villain Demographics")
            total_villains = villain_demo["Count"].sum()
            for _, row in villain_demo.iterrows():
                st.metric(
                    f"{row['Villain Race']} {row['Gender Villain']} Villains",
                    f"{row['Count']:,}",
                    f"Proportion: {row['Count'] / total_villains:.1%}"
                )

        with col2:
            st.markdown("### 📈 Key Insights")
            gender_distribution = villain_demo.groupby("Gender Villain")["Count"].sum()
            race_distribution = villain_demo.groupby("Villain Race")["Count"].sum()
            st.markdown(f"""
            - **Most common gender:** {gender_distribution.idxmax()} ({gender_distribution.max():,} villains)
            - **Most represented race:** {race_distribution.idxmax()} ({race_distribution.max():,} villains)
            - **Total villains analyzed:** {total_villains:,}
            """)

    section_description(
        """
        The heatmap paints a clear picture: white males <span class='red'>dominate</span> the villain roles in Hollywood, with
        women and people of color appearing far <span class='red'>less frequently</span>. This data isn’t just telling us who the
        villains are—it’s revealing the underlying patterns of exclusion.
        \n After all, you only need to look at the best-selling franchises to see a <span class='red'>white male</span> as the villain.""", margin_bottom="16em",
    )

    col1, col2, col3, col4 = st.columns(4)

    # Add images to each column
    with col1:
        st.image("static/friday_13th.jpg")
        st.markdown("<p style='text-align: center;'>Jason Vorhees<br>(Friday the 13th)</p>", unsafe_allow_html=True)

    with col2:
        st.image("static/halloween.jpg")
        st.markdown("<p style='text-align: center;'>Michael Meyers<br>(Halloween)</p>", unsafe_allow_html=True)

    with col3:
        st.image("static/childsplay.jpg")
        st.markdown("<p style='text-align: center;'>Chucky<br>(Child's Play)</p>", unsafe_allow_html=True)

    with col4:
        st.image("static/it.jpg")
        st.markdown("<p style='text-align: center;'>Pennywise<br>(IT)</p>", unsafe_allow_html=True)
    # Villain Gender Distribution as Horizontal Stacked Bars
