# Weather App using Python for Dockerization

A simple weather application built with Python, Flask, and the OpenWeather API. This app provides current weather information for a given city.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Setup](#docker-setup)
- [Environment Variables](#environment-variables)
- [License](#license)

## Project Overview

This application retrieves current weather data for a specified city using the OpenWeather API. It’s built with Flask, a lightweight web framework for Python.

## Installation

### Prerequisites

- Python 3.9 or later
- Docker (for containerization)

### Steps

1. **Clone the Repository**

   ```sh
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. **Install Dependencies**

   You can install dependencies using pip. It is recommended to use a virtual environment.

   ```sh
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

### Running Locally

To run the Flask application locally:

1. **Set Up Environment Variables**

   Create a `.env` file in the root directory with the following content:

   ```env
   OPENWEATHER_API_KEY=your_openweather_api_key
   ```

2. **Run the Application**

   ```sh
   python app.py
   ```

   The application will be available at `http://localhost:5000`.

### API Endpoint

- **GET** `/weather?city={city}`

  **Parameters:**
  - `city`: The name of the city for which to fetch the weather information.

  **Response:**
  ```json
  {
    "city": "City Name",
    "temperature": 20.5,
    "description": "clear sky"
  }
  ```

## Docker Setup

### Build and Run

1. **Create a `.env` File**

   Ensure you have a `.env` file in the root directory with your API key:

   ```env
   OPENWEATHER_API_KEY=your_openweather_api_key
   ```

2. **Build the Docker Image**

   ```sh
   docker-compose build
   ```

3. **Run the Docker Container**

   ```sh
   docker-compose up
   ```

   The application will be available at `http://localhost:5000`.

## Environment Variables

- `OPENWEATHER_API_KEY`: Your API key for accessing the OpenWeather API.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Replace `yourusername` with your actual GitHub username or repository URL, and `your_openweather_api_key` with your actual OpenWeather API key.

If you have additional sections or details you’d like to include, just let me know!
