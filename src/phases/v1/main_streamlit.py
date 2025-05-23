import streamlit as st
import pandas as pd
import math
import os
import dotenv
import requests

# Load environment variables
dotenv.load_dotenv()

# Predefined crops
VALID_CROPS = ["Corn", "Coffee"]
DATA_FILE = "data.csv"


# Function to read data from CSV
def load_from_csv():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        return df
    else:
        # Create empty dataframe with appropriate columns
        return pd.DataFrame({"Crop": [], "Area": [], "Input Needed": []})


# Function to save data to CSV
def save_to_csv(df):
    df.to_csv(DATA_FILE, index=False)


# Area calculation functions
def calculate_rectangle_area(length, width):
    return length * width


def calculate_circle_area(radius):
    return math.pi * radius**2


# Calculate required inputs based on crop and area
def calculate_inputs(crop, area):
    if crop == "Corn":
        return area * 200  # Example: 200kg/ha for Corn
    elif crop == "Coffee":
        return area * 0.5  # Example: 500mL/m² for Coffee
    return 0


# Weather API function
def get_weather_data(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        st.error("API key not found. Please set the WEATHER_API_KEY in .env file.")
        return None

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return weather_data
    else:
        return None


# Main Streamlit app
def main():
    st.set_page_config(page_title="Farm Tech Solutions", page_icon="🌱")

    st.title("🌱 Farm Tech Solutions")
    st.subheader("Crop Management and Weather Data")

    # Load existing data
    df = load_from_csv()

    # Tabs for different features
    tab1, tab2 = st.tabs(["Crop Management", "Weather Data"])

    # Tab 1: Crop Management
    with tab1:
        st.subheader("Manage Crop Data")

        # Form for adding new data
        with st.form("crop_data_form"):
            st.write("Add New Crop Data")

            # Input fields
            crop = st.selectbox("Select Crop:", VALID_CROPS)
            col1, col2 = st.columns(2)

            with col1:
                if crop == "Corn":
                    length = st.number_input(
                        "Length (m):", min_value=0.1, value=1.0, step=0.1
                    )
                else:
                    length = st.number_input(
                        "Radius (m):", min_value=0.1, value=1.0, step=0.1
                    )

            with col2:
                if crop == "Corn":
                    width = st.number_input(
                        "Width (m):", min_value=0.1, value=1.0, step=0.1
                    )
                else:
                    width = st.number_input(
                        "Width (not used for Coffee):",
                        min_value=0.1,
                        value=1.0,
                        step=0.1,
                        disabled=True,
                    )

            # Calculate button
            submitted = st.form_submit_button("Calculate and Add")

            if submitted:
                # Calculate area based on crop type
                if crop == "Corn":
                    area = calculate_rectangle_area(length, width)
                else:  # Coffee
                    area = calculate_circle_area(length)

                # Calculate inputs needed
                input_needed = calculate_inputs(crop, area)

                # Add to dataframe
                new_row = pd.DataFrame(
                    {"Crop": [crop], "Area": [area], "Input Needed": [input_needed]}
                )
                df = pd.concat([df, new_row], ignore_index=True)

                # Save to CSV
                save_to_csv(df)

                st.success(
                    f"Added new {crop} data with area {area:.2f} and input needed {input_needed:.2f}"
                )

        # Display existing data
        if not df.empty:
            st.subheader("Existing Crop Data")

            # Format the dataframe for display
            display_df = df.copy()
            display_df["Area"] = display_df["Area"].apply(lambda x: f"{x:.2f}")
            display_df["Input Needed"] = display_df["Input Needed"].apply(
                lambda x: f"{x:.2f}"
            )

            # Add an index column for row selection
            display_df.insert(0, "#", range(1, len(display_df) + 1))

            st.dataframe(display_df, use_container_width=True)

            # Actions for selected rows
            col1, col2 = st.columns(2)

            with col1:
                # Delete selected rows
                rows_to_delete = st.multiselect(
                    "Select rows to delete:",
                    options=list(range(1, len(df) + 1)),
                    format_func=lambda x: f"Row {x}",
                )

                if st.button(
                    "Delete Selected", type="primary", use_container_width=True
                ):
                    if rows_to_delete:
                        # Convert 1-based index to 0-based index
                        indices = [i - 1 for i in rows_to_delete]
                        df = df.drop(indices).reset_index(drop=True)
                        save_to_csv(df)
                        st.success(f"Deleted {len(rows_to_delete)} row(s)")
                        st.rerun()

            with col2:
                # Update row
                row_to_update = st.selectbox(
                    "Select a row to update:",
                    options=list(range(1, len(df) + 1)),
                    format_func=lambda x: f"Row {x}: {df.iloc[x-1]['Crop']}",
                )

                if st.button(
                    "Edit Selected Row", type="secondary", use_container_width=True
                ):
                    st.session_state.edit_row = row_to_update - 1  # Store 0-based index

            # Edit form appears when a row is selected for editing
            if "edit_row" in st.session_state:
                row_idx = st.session_state.edit_row
                row_data = df.iloc[row_idx]

                st.subheader(f"Edit Row {row_idx + 1}")

                with st.form("edit_form"):
                    edit_crop = st.selectbox(
                        "Crop:", VALID_CROPS, index=VALID_CROPS.index(row_data["Crop"])
                    )

                    col1, col2 = st.columns(2)
                    with col1:
                        if edit_crop == "Corn":
                            # For rectangle, we need to reverse-calculate length and width
                            # Since we only store area, we'll assume square (length = width) for simplicity
                            old_length = (
                                math.sqrt(row_data["Area"])
                                if edit_crop == "Corn"
                                else row_data["Area"] / math.pi
                            )
                            edit_length = st.number_input(
                                "Length (m):",
                                min_value=0.1,
                                value=float(old_length),
                                step=0.1,
                            )
                        else:
                            # For circle, we need to reverse-calculate radius
                            old_radius = math.sqrt(row_data["Area"] / math.pi)
                            edit_length = st.number_input(
                                "Radius (m):",
                                min_value=0.1,
                                value=float(old_radius),
                                step=0.1,
                            )

                    with col2:
                        if edit_crop == "Corn":
                            edit_width = st.number_input(
                                "Width (m):",
                                min_value=0.1,
                                value=float(old_length),
                                step=0.1,
                            )
                        else:
                            edit_width = st.number_input(
                                "Width (not used for Coffee):",
                                min_value=0.1,
                                value=1.0,
                                step=0.1,
                                disabled=True,
                            )

                    update_submitted = st.form_submit_button("Update")
                    cancel = st.form_submit_button("Cancel")

                    if update_submitted:
                        # Calculate new area and input needed
                        if edit_crop == "Corn":
                            new_area = calculate_rectangle_area(edit_length, edit_width)
                        else:
                            new_area = calculate_circle_area(edit_length)

                        new_input = calculate_inputs(edit_crop, new_area)

                        # Update the dataframe
                        df.at[row_idx, "Crop"] = edit_crop
                        df.at[row_idx, "Area"] = new_area
                        df.at[row_idx, "Input Needed"] = new_input

                        # Save changes
                        save_to_csv(df)

                        # Clear edit state and refresh
                        del st.session_state.edit_row
                        st.success("Row updated successfully!")
                        st.rerun()

                    if cancel:
                        del st.session_state.edit_row
                        st.rerun()
        else:
            st.info("No crop data available. Add some data using the form above.")

    # Tab 2: Weather Data
    with tab2:
        st.subheader("Weather Data")
        st.write("Get current weather information for any city.")

        city = st.text_input("Enter city name:", "Sao Paulo")

        if st.button("Get Weather Data"):
            weather_data = get_weather_data(city)

            if weather_data:
                col1, col2 = st.columns(2)

                with col1:
                    st.metric("Temperature", f"{weather_data['temperature']}°C")
                    st.metric("Humidity", f"{weather_data['humidity']}%")

                with col2:
                    st.metric("Wind Speed", f"{weather_data['wind_speed']} m/s")
                    st.metric("Conditions", weather_data["description"].capitalize())

                st.success(f"Current weather data for {city} retrieved successfully!")
            else:
                st.error(
                    f"Failed to retrieve weather data for {city}. Please check the city name and your API key."
                )


# Run the app
if __name__ == "__main__":
    main()
