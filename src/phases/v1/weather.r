# Load the libraries
library(httr)
library(jsonlite)

# Get the API key from the environment variables
api_key <- Sys.getenv("API_KEY")

# Check if the API key was loaded successfully
if (api_key == "") {
  stop("Error: API key not found. Make sure it is defined in the .env file.")
}

# Check if the city was provided as a command-line argument
args <- commandArgs(trailingOnly = TRUE)
if (length(args) == 0) {
  stop(
    "No city was provided. Please provide the city name as an argument."
  )
}

# Set the city based on the provided argument
city <- args[1]

# Define your API key and the desired city
units <- "metric" # To use Celsius

# Encode the city to ensure special characters don't cause issues
city_encoded <- URLencode(city)

# Build the API URL
url <- paste0(
  "https://api.openweathermap.org/data/2.5/weather?q=", city_encoded,
  "&appid=", api_key, "&units=", units
)

# Make the GET request to the API
response <- GET(url)

# Check if the request was successful
if (status_code(response) == 200) {
  # Parse the JSON response
  data <- fromJSON(content(response, as = "text"))

  # Extract the relevant information
  temperature <- data$main$temp
  description <- data$weather$description
  humidity <- data$main$humidity
  wind_speed <- data$wind$speed

  # Display the information in the terminal
  cat("City:", city, "\n")
  cat("Current temperature:", temperature, "°C\n")
  cat("Weather conditions:", description, "\n")
  cat("Humidity:", humidity, "%\n")
  cat("Wind speed:", wind_speed, "m/s\n")
} else {
  cat("Error fetching data. Status code:", status_code(response), "\n")
}
