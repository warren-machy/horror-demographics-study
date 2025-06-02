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
import os
from how_are_your_odds_looking import show_how_are_your_odds_looking
from title import show_title
from introduction import show_introduction
from landscape import show_villanous_landscape
from the_reaper_has_a_soft_spot_for_men import show_the_reaper_has_a_soft_spot_for_men
from non_white_prepare_to_die import show_non_white_prepare_to_die
from a_new_dawn_for_hollywood import show_a_new_dawn_for_hollywood
from resolution import show_resolution
import time

def load_css(file_path):
    try:
        with open(file_path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Warning: {file_path} not found")
        return ""


# Page Configuration
st.set_page_config(page_title="Does Grim Reaper Play Favorites? - Visualization Project", page_icon="🔪", layout="centered")


# Load CSS with error handling
css_path = "resources/styles.css"
css_content = load_css(css_path)
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
st.markdown(f"<style>{load_css('resources/styles.css')}</style>", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
>>>>>>> f6e1d2a01773c41f8f81ceec31f6cd47ce1c5133

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

show_title()

show_introduction()

show_villanous_landscape()

show_the_reaper_has_a_soft_spot_for_men()

show_non_white_prepare_to_die()

show_how_are_your_odds_looking()

show_a_new_dawn_for_hollywood()

show_resolution()

