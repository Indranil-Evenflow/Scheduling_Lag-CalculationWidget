# app.py

import streamlit as st
import pandas as pd
import plotly.express as px
from process_data import run_full_analysis
import io

st.set_page_config(layout="wide", page_title="Scheduling Lag Calculation Widget",     page_icon="evenflow_ai_logo.svg",
    initial_sidebar_state="expanded")

# Your Custom CSS
st.markdown("""
<style>
    /* Global styles */
    .main .block-container {padding: 2rem 2rem 2rem;}
    body {
        font-family: 'Segoe UI', sans-serif;
    }
    
    /* Title */
    h1 {
        color: #1a3c34;
        font-size: 2.5em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    /* Subtitle */
    .stMarkdown p {
        color: #4a5e6d;
        font-size: 1.1em;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Process Data Button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #50699c 0%, #3e557d 100%);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 12px 30px;
        font-size: 1.1em;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(80, 105, 156, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #3e557d 0%, #50699c 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(80, 105, 156, 0.4);
        color: white !important;
    }

    /* Download Results Button */
    .stDownloadButton>button {
        width: 100%;
        background: linear-gradient(90deg, #28a745 0%, #218838 100%);
        color: white !important;
        border-radius: 10px;
        padding: 10px 25px;
        font-size: 1em;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(40, 167, 69, 0.3);
    }
    .stDownloadButton>button:hover {
        background: linear-gradient(90deg, #218838 0%, #28a745 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(40, 167, 69, 0.4);
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- App UI ---

st.title("Scheduling Lag Calculation Widget")
st.markdown("Upload the 'Scheduling Lag (Planned Date - Created Date) -- EF' file from [Prod] Appointments (Qrvey) to generate report.")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Upload & Process")
    uploaded_file = st.file_uploader(
        "Choose a file (CSV or Excel)",
        type=['csv', 'xlsx', 'xls']
    )

    process_button = st.button("Analyse Data", disabled=(uploaded_file is None))


if process_button:
    with st.spinner('Analyzing your file... Hang tight!'):
        try:
            summary_df, output_path = run_full_analysis(uploaded_file)
            st.session_state['summary_df'] = summary_df
            st.session_state['output_path'] = output_path
            st.session_state['processed'] = True
        
        except Exception as e:
            st.error(f"An error occurred during processing: {e}")
            st.error("Please ensure your file has the correct columns ('scheduling_lag', 'evenflow_flag', 'active_appointment_count') and is not corrupted.")
            st.session_state['processed'] = False
    
    if st.session_state.get('processed', False):
        with col1:
            st.markdown("### Full Report")
            with open(st.session_state['output_path'], 'rb') as f:
                st.download_button(
                    label="Download Excel Report",
                    data=f,
                    file_name='Scheduling Lag Calculation Output.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )

        with col2:
            st.subheader("Percentage of Total: Within 1 Week ")
            summary_df = st.session_state['summary_df']
            
            display_df = summary_df.copy()
            for col in display_df.columns:
                if '%' in col:
                    display_df[col] = display_df[col].apply(lambda x: f'{x:.0%}' if pd.notnull(x) else 'N/A')
            
            st.dataframe(display_df.set_index('scheduling_lag'), use_container_width=True)

            chart_df = summary_df.melt(
                id_vars=['scheduling_lag'], 
                value_vars=[col for col in summary_df.columns if '%' in col],
                var_name='EvenFlow Category',
                value_name='Cumulative Percentage'
            )

            # --- MODIFIED CHART SECTION ---

            # 1. Prepare a text label column for the chart
            # This formats the numeric percentage (e.g., 0.55) into a display string (e.g., "55.0%")
            chart_df['text_label'] = chart_df['Cumulative Percentage'].apply(
                lambda x: f'{x:.0%}' if pd.notnull(x) else ''
            )

            # 2. Create the line chart, now passing the new 'text' column
            fig = px.line(
                chart_df,
                x='scheduling_lag',
                y='Cumulative Percentage',
                color='EvenFlow Category',
                markers=True,
                text='text_label',  # Use the formatted text for data labels
                title='Cumulative Percentage Growth by Scheduling Lag',
                labels={'scheduling_lag': 'Scheduling Lag (Days)', 'Cumulative Percentage': 'Cumulative % of Total'}
            )

            # 3. Update layout and traces to position the text labels neatly
            fig.update_layout(
                xaxis_title="Scheduling Lag (Days)",
                yaxis_title="Cumulative Percentage",
                legend_title="EvenFlow Flag",
                yaxis_tickformat='.0%'
            )
            fig.update_traces(
                textposition='top center' # Position the text just above the marker
            )

            # --- END OF MODIFIED CHART SECTION ---
            
            st.plotly_chart(fig, use_container_width=True)

            st.markdown("""
                <div class="footer">
                    An EvenFlow AI Tool (Version 1.0) - All rights reserved 2025
                </div>
            """, unsafe_allow_html=True)
