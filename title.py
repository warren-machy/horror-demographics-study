import streamlit as st

def show_title():
    st.markdown(
    """
    <style>
    /* General Reset */
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    html, body {
        width: 100%;
        height: 100%;
    }

    /* Full-screen container for vertical centering */
    .full-screen-container {
        margin-top: -15%;
        display: flex;
        flex-direction: column; /* Stack title, line, subtitle, and scroll indicator */
        justify-content: center; /* Center vertically */
        align-items: center; /* Center horizontally */
        height: 100vh; /* Full viewport height */
        overflow: hidden; /* Prevent scroll on the main container */
    }

    /* Fade-in animation */
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }

    /* Line Expand Animation */
    @keyframes lineExpand {
        0% { width: 0; }
        100% { width: 10%; }
    }

    /* Super Title Styling */
    .super-title {
        text-align: center;
        font-size: 1em;
        font-weight: lighter;
        color: #eee; /* Light text for contrast */
        opacity: 0; /* Initially invisible */
        margin-bottom: 0.5em;
        user-select: none;
        animation: fadeIn 1s ease-in forwards; /* Fade in immediately */
    }

    /* Main Title Styling */
    .center-title {
        text-align: center;
        font-size: 2.1em;
        font-weight: bold;
        color: #eee; /* Light text for contrast */
        opacity: 0; /* Initially invisible */
        user-select: none;
        animation: fadeIn 1s ease-in forwards; /* Fade in with delay */
        animation-delay: 2s; /* Start after Super Title */
    }

    /* Expanding Line Styling */
    .expanding-line {
        margin: 0 auto; /* Center align */
        margin-top: 0.5em;
        height: 1px; /* Line height */
        background-color: #eee; /* Light line */
        width: 0; /* Start at zero width */
        opacity: 0; /* Initially invisible */
        animation: fadeIn 1s ease-in forwards, lineExpand 1s ease-out forwards;
        animation-delay: 2.5s; /* Start after the main title */
    }

    /* Subtitle Styling */
    .sub-title {
        text-align: center;
        font-size: 0.8em;
        font-weight: lighter;
        color: #eee; /* Light text for subtitle */
        opacity: 0; /* Initially invisible */
        margin-top: 1.3em;
        user-select: none;
        animation: fadeIn 1s ease-in forwards; /* Fade in with delay */
        animation-delay: 3.5s; /* Start after the line */
    }

    /* Scrolling Indicator Styling */
    .scroll-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 2em;
    }

    .mouse {
        width: 30px;
        height: 70px;
        border: 2px solid #fff; /* White border for the mouse icon */
        border-radius: 60px;
        position: relative;
        opacity: 0; /* Initially invisible */
        animation: fadeIn 1s ease-in forwards;
        animation-delay: 4s; /* Start after subtitle */
    }

    .mouse::before {
        content: '';
        width: 12px;
        height: 12px;
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        background-color: #fff; /* White inner circle */
        border-radius: 50%;
        opacity: 1;
        animation: wheel 2s infinite;
    }

    @keyframes wheel {
        to {
            opacity: 0;
            top: 50px;
        }
    }

    @keyframes down {
        0% {
            transform: translateY(0);
        }
        20% {
            transform: translateY(15px);
        }
        40% {
            transform: translateY(0);
        }
    }
    </style>

    <div class="full-screen-container">
        <div>
            <div class="super-title">Visualization Project</div>
            <div class="center-title">DOES THE GRIM REAPER PLAY FAVORITES?</div>
            <div class="expanding-line"></div>
            <div class="sub-title">Made with ❤ by the horror movie team</div>
        </div>
        <div class="scroll-container">
            <div class="mouse"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)