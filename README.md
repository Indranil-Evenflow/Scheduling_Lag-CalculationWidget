# Scheduling Lag Calculation Widget

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://scheduling-lag-calculation-widget.streamlit.app/)

A user-friendly web application built with Streamlit designed for non-technical teams to instantly analyze appointment scheduling efficiency. The tool automatically processes raw data exports, handles messy file formats, and generates an interactive report with visualizations and a downloadable Excel summary.


*The clean and professional dashboard interface.*

---

## ✨ Key Features

*   **🧠 Intelligent File Parsing:** Automatically detects header rows, even in files with metadata at the top.
*   **📂 Multi-format Support:** Accepts both `.csv` and `.xlsx` files with various delimiters (comma or tab).
*   **⚙️ Automated Analysis:** Performs all required calculations, including pivoting, grand totals, and cumulative percentages.
*   **📊 Interactive Visualizations:** Displays a clean bar chart using Plotly for easy comparison of performance.
*   **📥 One-Click Export:** Generates a comprehensive, professionally formatted multi-sheet Excel report for download.
*   **🛡️ Robust Error Handling:** Guides the user with clear messages if the file format is incorrect or corrupted.

## 🚀 How to Use the Live App

1.  **Navigate** to the application URL: [scheduling-lag-calculation-widget.streamlit.app](https://scheduling-lag-calculation-widget.streamlit.app/)
2.  **Upload** your raw appointment data file using the file uploader in the sidebar.
3.  **Click** the "Analyze Data" button.
4.  **View** the interactive KPI metrics, chart, and data summary on the dashboard.
5.  **Download** the full, formatted report as an Excel file.

---

## 🛠️ Local Setup and Installation

To run this application on your local machine, follow these steps.

### Prerequisites

*   Python 3.9+
*   `pip` package manager

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Indranil-Evenflow/Scheduling_Lag-CalculationWidget.git
    cd Scheduling_Lag-CalculationWidget
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    The application will open in your default web browser.

## ⚙️ Technology Stack

*   **Frontend & UI:** Streamlit
*   **Data Manipulation:** Pandas & NumPy
*   **File Parsing:** OpenPyXL
*   **Data Visualization:** Plotly Express
