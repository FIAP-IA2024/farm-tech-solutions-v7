# Automatically load environment variables from the .env file
if (file.exists(".env")) {
  library(dotenv)
  dotenv::load_dot_env()
}

# Automatically activate the renv environment
if (file.exists("renv/activate.R")) {
  source("renv/activate.R")
}
