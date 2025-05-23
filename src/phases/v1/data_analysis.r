# Install and load necessary packages
library(dplyr)
library(ggplot2)

# Load data from the CSV file
data <- read.csv("data.csv")

# View the first records
head(data)

# Calculate the mean and standard deviation of the 'Area' column
mean_area <- mean(data$Area)
sd_area <- sd(data$Area)

# Calculate the mean and standard deviation of the 'Input Needed' column
mean_input <- mean(data$Input.Needed)
sd_input <- sd(data$Input.Needed)

# Display the results
cat("\nMean Planting Area:", mean_area, "\n")
cat("Standard Deviation of Planting Area:", sd_area, "\n")
cat("Mean of Inputs Needed:", mean_input, "\n")
cat("Standard Deviation of Inputs Needed:", sd_input, "\n")

# Visualizations: Adjusted Histogram of Planting Area with appropriate binwidth
png("histogram_area.png")
ggplot(data, aes(x = Area)) +
  geom_histogram(
    binwidth = max(data$Area) / 30,
    fill = "blue",
    color = "black",
    alpha = 0.7
  ) +
  labs(title = "Distribution of Planting Area", x = "Area", y = "Frequency")

# Visualizations: Boxplot of Inputs Needed
png("boxplot_inputs_needed.png")
ggplot(data, aes(x = "", y = Input.Needed)) +
  geom_boxplot(fill = "green", color = "black", alpha = 0.7) +
  labs(title = "Boxplot of Inputs Needed", y = "Inputs (mL/kg)")

# Outlier Analysis: Using IQR for 'Area'
iqr_area <- IQR(data$Area)
lower_bound_area <- quantile(data$Area, 0.25) - 1.5 * iqr_area
upper_bound_area <- quantile(data$Area, 0.75) + 1.5 * iqr_area
outliers_area <- data %>% filter(
  Area < lower_bound_area | Area > upper_bound_area
)

# Outlier Analysis: Using IQR for 'Input Needed'
iqr_input <- IQR(data$Input.Needed)
lower_bound_input <- quantile(data$Input.Needed, 0.25) - 1.5 * iqr_input
upper_bound_input <- quantile(data$Input.Needed, 0.75) + 1.5 * iqr_input
outliers_input <- data %>% filter(
  Input.Needed < lower_bound_input | Input.Needed > upper_bound_input
)

# Display Outliers
cat("\nOutliers in Planting Area:\n")
print(outliers_area)
cat("\nOutliers in Inputs Needed:\n")
print(outliers_input)
