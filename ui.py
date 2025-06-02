import streamlit as st

def section_title(text: str, margin_top: str = "0", margin_bottom: str = "0"):
    st.markdown(
        f"""
        <style>
            .title {{
                font-size: 1.9em;
                font-weight: normal;
                color: #eee;
                margin-top: {margin_top};
                margin-bottom: {margin_bottom};
                padding-top: 30px;
                padding-bottom: 30px;
                user-select: none;
            }}
            .title:after {{
                content: '';
                display: block;
                width: 10%;
                height: 2px;
                background-color: #eee;
                margin-top: 0em;
                margin-left: 0;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(f"""<div class="title">{text}</div>""", unsafe_allow_html=True)

def section_description(text: str, margin_top: str = "0", margin_bottom: str = "0em"):
    st.markdown(
        f"""
        <style>
            .description {{
                font-size: 1.1em;
                font-weight: lighter;
                color: #eee;
                margin-top: {margin_top};
                margin-bottom: {margin_bottom};
                user-select: none;
                padding-bottom: 30px;
            }}
            .red {{
                color: #FF1D1D;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(f"""<div class="description">{text}</div>""", unsafe_allow_html=True)

def styled_image(image_path: str, margin_top: str = "0px", margin_bottom: str = "0px"):
    # CSS for margin styling
    st.markdown(
        f"""
        <style>
            .image-container {{
                margin-top: {margin_top};
                margin-bottom: {margin_bottom};
                text-align: center;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    # Wrap st.image in a div with a custom class
    st.markdown(f'<div class="image-container">', unsafe_allow_html=True)
    st.image(image_path)  # Display the image
    st.markdown('</div>', unsafe_allow_html=True)  # Close the div

