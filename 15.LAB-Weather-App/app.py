from flask import Flask, request, jsonify
import requests
import os
from urllib.parse import quote as url_quote

app = Flask(__name__)

# Fetch API key from environment variables
API_KEY = os.getenv('OPENWEATHER_API_KEY')

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    if not API_KEY:
        return jsonify({"error": "API key not found"}), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?q={url_quote(city)}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Unable to fetch weather data"}), 500

    data = response.json()
    return jsonify({
        "city": data['name'],
        "temperature": data['main']['temp'],
        "description": data['weather'][0]['description']
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

