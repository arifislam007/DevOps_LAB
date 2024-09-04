# Weather App using Python for Dockerization

A simple weather application built with Python, Flask, and the OpenWeather API. This app provides current weather information for a given city.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Setup](#docker-setup)

## Project Overview

This application retrieves current weather data for a specified city using the OpenWeather API. It’s built with Flask, a lightweight web framework for Python.

## Installation

### Prerequisites

- Python 3.9 or later
- Docker (for containerization)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/arifislam007/DevOps_LAB.git
   cd weather-app/15.LAB (Python_Weather_API)

   ```

2. **Install Dependencies**


   ```sh
      Flask==2.1.3
      Werkzeug==2.3.0
      requests==2.28.2
   ```

## Usage: Build a Docker image

   ```sh
      docker build -t MyPython_app:v1 .
   ```

## Run Docker Container with the image and API Key

   ```bash
   docker run -itd --name weatherAPI -e OPENWEATHER_API_KEY=YourAPIKeyPlaceHere -p 8080:5000 MyPython_app:v1
   ```

## Run the Application
just browse to your docker host ip: **YourDockerHostIP:8080/weather?city=Dhaka </br>
for me its http://10.200.205.187:8080/weather?city=Dhaka

