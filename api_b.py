from flask import Flask, jsonify

app = Flask(__name__)

mock_weather_data = {
    "saopaulo": 25,
    "riodejaneiro": 35,
    "curitiba": 14,
    "portoalegre": 18,
    "salvador": 31
}

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    city_key = city.replace(" ", "").replace("-", "").lower()

    temperature = mock_weather_data.get(city_key)

    if temperature is not None:
        return jsonify({
            "city": city,
            "temp": temperature,
            "unit": "Celsius"
        })
    else:
        return jsonify({"error": "Cidade não encontrada"}), 404

if __name__ == '__main__':
    app.run(port=5001)
