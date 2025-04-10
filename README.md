# NYC Taxi Data and AI Integration - Find top 5 trips where trip duration was more than normal

This app integrates the NYC Taxi dataset with AI-powered functionalities:
- **SQL Generator**: Allows users to generate SQL queries dynamically based on their input.
- **Image Generator**: Uses Stable Diffusion or other AI models to generate images based on a description.
- **Data Query**: Queries the NYC taxi dataset using SQL and displays the results.

## Requirements
- Python 3.9+
- Streamlit
- DuckDB (for querying the dataset)
- Stable Diffusion (for image generation)

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run NIM - 
   1. docker run --gpus all -p 5000:5000 nvcr.io/nvidia/nim/sql-generation:latest
   2. docker run --gpus all -p 5001:5001 nvcr.io/nvidia/nim/text-to-image:latest 
3. Run the app: `streamlit run app/main.py`

## Docker
To run the app in a Docker container:
1. Build the image: `docker build -t nyc-taxi-nim-ai .`
2. Run the container: `docker run -p 8501:8501 nyc-taxi-nim-ai`
