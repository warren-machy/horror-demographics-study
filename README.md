<div align="center">
  <img src="static/header_gitlab.png" alt="Main Poster">
</div>

# 🎥 Does the Grim Reaper Play Favorites? – A Horror Movie Visualization Project

<div align="center">
  <h2>👻 Unmasking Biases in Hollywood's Most Terrifying Genre</h2>
</div>

<div align="center">
    <p>
        <a href="#introduction-and-motivation">Introduction and Motivation</a> •
        <a href="#how-to-setup">How to Setup</a> •
        <a href="#showcase">Showcase</a>     
    </p>
</div>

## Introduction and Motivation

Horror has become the fastest-growing film genre, with its market share more than doubling from 4.87% in 2013 to 10.08% in 2023. However, a closer look at iconic films from past decades, such as *Friday the 13th*, reveals a troubling pattern:

* **Males** are more likely to die or take on villainous roles
* **Women** are often underrepresented as protagonists
* **People of color** are less frequent in horror films, and when they do appear, they are disproportionately likely to die

In light of these observations, our team has decided to conduct an analysis of gender, race, and violence in horror films. By examining patterns across various films from different periods, we aim to uncover the societal implications and biases embedded in the genre, and explore how these have evolved over time—whether for better or for worse.

This project dives into **89 years of horror movie data** (1931–2024) with a primary focus on **1980–2024**, to reveal how **gender, race, and violence** intersect in one of the most iconic film genres. We built an interactive web app to present these insights in a **story-driven visualization experience**.

The primary goal of this project is to raise awareness among the general public, as well as provide a concise summary of gender and racial biases for researchers, filmmakers, and anyone interested in understanding the dynamics within horror movies.

### 🔍 Key Features

* 📊 **Interactive Visualizations** exploring protagonist/villain trends by race and gender
* 💀 **Death Probability Simulator** – input your demographics to predict your odds in a horror movie
* 🔥 Data-driven storytelling from classic tropes to modern breakthroughs
* 🎬 Case studies from *Get Out*, *Ma*, *Us*, and *MaXXXine*

## How to Setup

You can launch the app locally using Streamlit:

```bash
pip install -r requirements.txt
streamlit run app.py
```

🐳 Want to run it in Docker?

```bash
docker build -t horror-viz .
docker run -p 8501:8501 horror-viz
```

### 📁 Project Structure

```
├── app.py                           # Main Streamlit app
├── data/                            # CSV dataset (Demographics + Outcomes)
├── static/                          # Movie images used in visualizations
├── *.py                             # Section-wise visualization modules
├── Dockerfile                       # Container config
├── resources/styles.css             # Custom styling
└── README.md                        # You are here
```

## Showcase

| Section | Description |
|---------|-------------|
| **The Villainous Landscape** | Heatmap of gender and race of villains in blockbuster horror |
| **The Reaper Has a Soft Spot for Men** | Examines gendered death rates |
| **Non-White? Prepare to Die!** | Death rates of white vs non-white characters |
| **A New Dawn for Hollywood** | Rise of female and non-white protagonists |
| **How Are Your Odds Looking?** | Try-it-yourself prediction tool based on demographic input |

### Key Features

* 📊 **Interactive Visualizations** exploring protagonist/villain trends by race and gender
* 💀 **Death Probability Simulator** – input your demographics to predict your odds in a horror movie
* 🔥 Data-driven storytelling from classic tropes to modern breakthroughs
* 🎬 Case studies from *Get Out*, *Ma*, *Us*, and *MaXXXine*
* Data analysis and insights on representation in horror movies
* Visualization tools to highlight trends and biases
* A critical exploration of how these trends influence public perception and media

### 📚 Data Source

The dataset was manually scraped from the **Dead Meat Wiki** using automated Selenium scripts. It includes:
* Character demographics (gender, race)
* Role classification (villain, protagonist, etc.)
* Survival and death outcomes
* Movie metadata (title, release year)

### ✨ Inspiration

This project was created as part of a **visualization and storytelling course**. It was driven by the question:

*"Do horror films mirror societal bias, or are they rewriting it?"*

We hope it contributes to broader discussions about **equity and diversity in media**.

### 📢 License

MIT License – free to use and build upon.



