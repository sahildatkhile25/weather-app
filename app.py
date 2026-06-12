from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "8b6ce940b9fa3800bc95974157799360"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind": data["wind"]["speed"]
    }

    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)