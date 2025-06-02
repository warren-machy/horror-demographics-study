# This file is a template, and might need editing before it works on your project.
# This file is a template, and might need editing before it works on your project.
FROM python:3.12-slim


# Set working directory
WORKDIR /app

COPY * /app

RUN pip install -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# For some other command
CMD ["streamlit", "run", "app.py"]
