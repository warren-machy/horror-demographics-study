import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from ui import *

def show_introduction():
    section_title("Introduction", margin_bottom="5em")
    st.markdown(f'<div class="image-container">', unsafe_allow_html=True)
    styled_image("static/intro-1.jpg", margin_top="-20px")
    styled_image("static/intro-2.jpg")
    styled_image("static/intro-3.jpg")