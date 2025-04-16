from flask import Flask, jsonify
import requests

app = Flask(__name__)

API_B_URL = 'http://localhost:5001/weather/'  # URL da API B

@app.route('/recommendation/<city>', methods=['GET'])
def get_recommendation(city):
    try:
        # Faz a chamada à API B
        response = requests.get(f"{API_B_URL}{city}")
        
        if response.status_code != 200:
            return jsonify({"error": "Cidade não encontrada na API B"}), 404

        data = response.json()
        temp = data['temp']

        # Gera recomendação baseada na temperatura
        if temp > 30:
            recommendation = "Está bem quente! Hidrate-se e use protetor solar."
        elif 15 < temp <= 30:
            recommendation = "Clima agradável! Aproveite o dia."
        else:
            recommendation = "Está frio. Leve um casaco!"

        return jsonify({
            "city": data['city'],
            "temp": temp,
            "unit": data['unit'],
            "recommendation": recommendation
        })

    except Exception as e:
        return jsonify({"error": "Erro ao consultar a API B", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5002)
