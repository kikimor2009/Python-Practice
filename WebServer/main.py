from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/ping")
# for more complicated scenario use 'render_template' library
def ping():
    return "<h1>PONG</h1>"

@app.route("/health")
def health():
    return jsonify(health='HELATH')

#Params for API query
api_key = 'a6311858fb35df63b55216bae4aa952a'
mode = 'html'
#Create a list of tuppels 
coordinates = []
# Add London coordinates
coordinates.append((51.507359,-0.136439))

@app.route("/")
def index():
    endpoint = f"https://api.openweathermap.org/data/2.5/weather?lat={coordinates[0][0]}&lon={coordinates[0][1]}&appid={api_key}&mode={mode}"
    response = requests.get(endpoint)
    return response.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
