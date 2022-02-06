from flask import Flask, Response
import Adafruit_DHT
import json

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 14
ROUND = 1
PORT = 8080

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/get', methods=["GET"])
def get_hum_temp():
    hum, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temp = round(temp, ROUND)
    hum = round(hum, ROUND)
    data = [temp, hum]
    return Response(json.dumps(data), mimetype = 'application/json')

if __name__ == '__main__':
    app.run('0.0.0.0', port = PORT)
