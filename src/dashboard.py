import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import importlib.util
import subprocess
import tempfile
from pathlib import Path

# Add project root to path for proper imports
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Paths to phase modules
PHASE1_PATH = Path(__file__).parent / 'phases' / 'v1'
PHASE2_PATH = Path(__file__).parent / 'phases' / 'v2'
PHASE3_PATH = Path(__file__).parent / 'phases' / 'v3'
PHASE6_PATH = Path(__file__).parent / 'phases' / 'v6'

# Import modules dynamically
def import_module_from_file(module_name, file_path):
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None:
            return None
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        st.error(f"Error importing {module_name} from {file_path}: {e}")
        return None

# Configure page
st.set_page_config(
    page_title="FarmTech System - Integrated Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add sidebar
st.sidebar.title("FarmTech System")
st.sidebar.subheader("Integrated Dashboard")
st.sidebar.markdown("---")

# Main content
st.title("🌱 FarmTech System - Integrated Dashboard")
st.markdown(
    """
    This dashboard integrates multiple phases of the FarmTech project:
    - **Phase 1**: Planting area calculation and weather data ingestion
    - **Phase 2**: Relational database structure and models
    - **Phase 3**: Simulated IoT irrigation logic
    - **Phase 6**: Image analysis using computer vision
    
    Select a phase from the tabs below to interact with its functionality.
    """
)

# Create tabs for each phase
tab1, tab2, tab3, tab6 = st.tabs(["Phase 1: Planting & Weather", "Phase 2: Database", "Phase 3: IoT Irrigation", "Phase 6: Computer Vision"])

# Phase 1: Planting area calculation and weather data
with tab1:
    st.header("Phase 1: Planting Area & Weather Data")
    st.markdown(
        """
        This phase calculates planting areas and manages crop data. It also provides weather data through the OpenWeather API.
        """
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Crop Management")
        
        if st.button("Run Crop Management Tool", key="run_phase1_main"):
            try:
                # We'll execute the main.py script from Phase 1
                # Since it's a GUI application, we'll inform the user
                st.info("The Crop Management Tool is a GUI application that will be launched in a separate window.")
                
                # Execute the script in a subprocess
                process = subprocess.Popen(
                    [sys.executable, str(PHASE1_PATH / "main.py")],
                    cwd=str(PHASE1_PATH),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                
                # Show a success message
                st.success("Crop Management Tool launched! Check the separate window that opened.")
                
                # Display any output or errors
                stdout, stderr = process.communicate()
                if stdout:
                    st.code(stdout)
                if stderr:
                    st.error(stderr)
            except Exception as e:
                st.error(f"Error running Crop Management Tool: {e}")
    
    with col2:
        st.subheader("Weather Data")
        city = st.text_input("Enter city name for weather data:", "Sao Paulo")
        
        if st.button("Get Weather Data", key="run_phase1_weather"):
            try:
                # Execute the weather.r script from Phase 1
                with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as temp_file:
                    process = subprocess.Popen(
                        ["Rscript", str(PHASE1_PATH / "weather.r"), city],
                        cwd=str(PHASE1_PATH),
                        stdout=temp_file,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    
                    stderr = process.communicate()[1]
                    if process.returncode != 0:
                        st.error(f"Error running weather script: {stderr}")
                    else:
                        # Read the results from the temp file
                        temp_file.close()
                        with open(temp_file.name, 'r') as f:
                            weather_data = f.read()
                        
                        # Display the weather data
                        st.success(f"Weather data for {city}:")
                        st.write(weather_data)
                        
                        # Clean up
                        os.unlink(temp_file.name)
            except Exception as e:
                st.error(f"Error getting weather data: {e}")

# Phase 2: Database Structure
with tab2:
    st.header("Phase 2: Database Structure")
    st.markdown(
        """
        This phase provides the relational database structure for managing agricultural inputs.
        """
    )
    
    # Display the database diagram
    st.subheader("Database Entity-Relationship Diagram")
    diagram_path = PHASE2_PATH / "diagram.png"
    if diagram_path.exists():
        st.image(str(diagram_path), caption="Database Entity-Relationship Diagram")
    else:
        st.warning("Database diagram not found.")
    
    # Show SQL Schema
    st.subheader("SQL Schema")
    sql_path = PHASE2_PATH / "data-model.sql"
    if sql_path.exists():
        with open(sql_path, 'r') as f:
            sql_content = f.read()
        st.code(sql_content, language="sql")
    else:
        st.warning("SQL schema file not found.")

# Phase 3: IoT Irrigation
with tab3:
    st.header("Phase 3: IoT Irrigation Logic")
    st.markdown(
        """
        This phase simulates IoT devices for monitoring and controlling irrigation systems.
        """
    )
    
    # Import the necessary modules from Phase 3
    try:
        # Add Phase 3 to path
        sys.path.append(str(PHASE3_PATH / "app"))
        
        # Try to import the modules
        weather_module = import_module_from_file("weather", str(PHASE3_PATH / "app" / "weather.py"))
        database_module = import_module_from_file("database", str(PHASE3_PATH / "app" / "database.py"))
        
        if weather_module and database_module:
            # Weather data
            st.subheader("Weather Data")
            city = st.text_input("Enter city name:", "Sao Paulo")
            
            if st.button("Get Weather Data", key="run_phase3_weather"):
                try:
                    weather_data = weather_module.get_weather_data(city)
                    if weather_data:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Temperature (°C)", weather_data["temperature"])
                        with col2:
                            st.metric("Humidity (%)", weather_data["humidity"])
                        st.write(f"Description: {weather_data['description'].capitalize()}")
                    else:
                        st.warning("Could not retrieve weather data. Check the city name.")
                except Exception as e:
                    st.error(f"Error getting weather data: {e}")
            
            # Sensor data
            st.subheader("Sensor Data")
            if st.button("Load Sensor Data", key="run_phase3_sensors"):
                try:
                    sensor_data = database_module.fetch_sensor_data()
                    if not sensor_data.empty:
                        st.dataframe(sensor_data)
                        
                        # Display some visualizations
                        st.subheader("Sensor Data Visualizations")
                        
                        # Group by month
                        monthly_data = sensor_data.groupby("month").mean().reset_index()
                        
                        # Humidity chart
                        fig, ax = plt.subplots(figsize=(10, 4))
                        ax.plot(monthly_data["month"].astype(str), monthly_data["humidity"], marker="o")
                        ax.set_xlabel("Month")
                        ax.set_ylabel("Average Humidity (%)")
                        ax.set_title("Monthly Average Humidity")
                        st.pyplot(fig)
                    else:
                        st.warning("No sensor data available.")
                except Exception as e:
                    st.error(f"Error loading sensor data: {e}")
        else:
            st.warning("Could not load the necessary modules from Phase 3.")
    except Exception as e:
        st.error(f"Error initializing Phase 3 components: {e}")

# Phase 6: Computer Vision
with tab6:
    st.header("Phase 6: Computer Vision for Agriculture")
    st.markdown(
        """
        This phase implements computer vision using YOLO for object detection in agricultural applications.
        """
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Run Object Detection")
        epochs = st.slider("Number of epochs", min_value=10, max_value=100, value=30, step=10)
        batch_size = st.slider("Batch size", min_value=4, max_value=32, value=16, step=4)
        
        if st.button("Run Object Detection Training", key="run_phase6"):
            try:
                st.info("Starting YOLO object detection training... This may take a while.")
                
                # Execute the Python script from Phase 6
                with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as temp_file:
                    process = subprocess.Popen(
                        [
                            sys.executable, 
                            str(PHASE6_PATH / "notebooks" / "GabrielRibeiro_rm560173_pbl_fase6.py"),
                            "--epochs", str(epochs),
                            "--batch-size", str(batch_size)
                        ],
                        cwd=str(PHASE6_PATH),
                        stdout=temp_file,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    
                    # Show a progress message
                    st.info("Object detection training in progress. Please wait...")
                    stderr = process.communicate()[1]
                    
                    # Read the results
                    temp_file.close()
                    with open(temp_file.name, 'r') as f:
                        output = f.read()
                    
                    if process.returncode != 0:
                        st.error(f"Error running object detection: {stderr}")
                    else:
                        st.success("Object detection training completed successfully!")
                        st.code(output)
                    
                    # Clean up
                    os.unlink(temp_file.name)
            except Exception as e:
                st.error(f"Error running object detection: {e}")
    
    with col2:
        st.subheader("View Results")
        st.markdown(
            """
            After running the object detection, the results will be saved in the results directory.
            You can find:
            - Training metrics
            - Validation results
            - Test predictions
            - Performance analysis
            """
        )
        
        # Check if results directory exists and list available result folders
        results_dir = PHASE6_PATH / "results"
        if results_dir.exists() and results_dir.is_dir():
            result_folders = [f for f in results_dir.iterdir() if f.is_dir()]
            if result_folders:
                selected_result = st.selectbox(
                    "Select a result to view:",
                    options=[f.name for f in result_folders],
                    index=0
                )
                
                # Display some images from the selected result folder
                selected_path = results_dir / selected_result
                image_files = list(selected_path.glob("*.png")) + list(selected_path.glob("*.jpg"))
                
                if image_files:
                    selected_image = st.selectbox(
                        "Select an image to view:",
                        options=[img.name for img in image_files],
                        index=0
                    )
                    
                    st.image(
                        str(selected_path / selected_image),
                        caption=selected_image,
                        use_column_width=True
                    )
                else:
                    st.info("No image results found in this folder.")
            else:
                st.info("No results available. Run the object detection first.")
        else:
            st.info("Results directory not found. Run the object detection first.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>FarmTech System - Integrated Dashboard</p>
        <p>© 2025 FIAP</p>
    </div>
    """,
    unsafe_allow_html=True
)
