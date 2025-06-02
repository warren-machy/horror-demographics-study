import streamlit as st
import streamlit.components.v1 as components

# Add your header
st.markdown('<h1 style="text-align: center;">Introduction - Comic Drawing</h1>', unsafe_allow_html=True)

# Embed the images and JavaScript using components.html
components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }
        .fade-in {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 1s ease-out, transform 1s ease-out;
        }
        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }
        .content {
            max-width: 800px;
            margin: 20px auto;
            text-align: center;
        }
        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <div class="content fade-in">
        <img src="intro-1.jpg" alt="Introduction Image 1">
    </div>
    <div class="content fade-in">
        <img src="intro-2.jpg" alt="Introduction Image 2">
    </div>
    <div class="content fade-in">
        <img src="intro-3.jpg" alt="Introduction Image 3">
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                    }
                });
            });

            document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
        });
    </script>
</body>
</html>
""", height=800, scrolling=True)
