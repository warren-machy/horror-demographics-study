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

def show_resolution():
    section_title("Resolution")
    section_description(
        """
    This rise of female and non-white protagonists and villains is not just a trend—it’s a <span class='red'>revolution</span> in the making. 
    It's a hopeful reminder that Hollywood is beginning to reflect the <span class='red'>diverse</span> world we live in, 
    where people of all backgrounds, genders, and races can see themselves as the heroes and villains of their own stories.
    \n\nThis is the future of storytelling, one where every character, regardless of gender or race, 
    has the chance to lead, to fight, and to thrive.
    """)
    st.image("static/minimized.jpg")