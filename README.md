## Scheduling Lag Analysis Dashboard

![alt text](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)


![alt text](https://img.shields.io/badge/python-3.9+-blue.svg)


![alt text](https://img.shields.io/badge/License-MIT-yellow.svg)

An intelligent web application that automates the analysis of appointment scheduling lag. This tool ingests complex data files from system exports, dynamically finds the relevant data, and produces a clean, interactive report with downloadable insights.

🚀 Live Demo

Experience the live application here:

➡️ scheduling-lag-calculation-widget.streamlit.app

✨ Key Features

Dynamic Header Detection: Intelligently scans files to find the true data table, skipping metadata and empty rows.

Multi-Format Support: Seamlessly processes .csv and .xlsx files, automatically detecting tab or comma separators.

Automated Data Cleaning: Handles common data issues, like numbers with commas (109,874), ensuring accurate calculations.

Interactive Visualizations: Generates an interactive bar chart using Plotly to visualize cumulative percentages over time.

Full Report Generation: Produces a comprehensive, multi-sheet Excel report with the raw data and all analysis tables.

Elegant User Interface: A clean, modern, and intuitive interface built with Streamlit.

🛠️ Technology Stack

Frontend: Streamlit

Data Processing: Pandas, NumPy

Excel/File Handling: Openpyxl

Visualization: Plotly Express

⚙️ Setup and Local Installation

To run this application on your local machine, follow these steps:

Clone the repository:

code
Bash
download
content_copy
expand_less

git clone https://github.com/your-username/scheduling-lag-dashboard.git
cd scheduling-lag-dashboard

Create and activate a virtual environment:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

Install the required dependencies:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
pip install -r requirements.txt

(Note: You will need to create a requirements.txt file containing streamlit, pandas, numpy, openpyxl, and plotly.)

Run the Streamlit application:

code
Bash
download
content_copy
expand_less
IGNORE_WHEN_COPYING_START
IGNORE_WHEN_COPYING_END
streamlit run app.py

Your browser will automatically open with the local version of the app.

📂 Project Structure

The project is structured to separate the core logic from the user interface for maintainability:

process_data.py: Contains all the robust backend logic for file reading, data cleaning, and table generation.

app.py: Contains all the Streamlit code for the front-end user interface, visualizations, and user interactions.

requirements.txt: Lists all the project dependencies.

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
