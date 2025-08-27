import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json
from flask_cors import CORS
# from pymongo import MongoClient

load_dotenv()
IP = os.getenv("IPV4")
DB = os.getenv("DB")
# client = MongoClient()
# client = MongoClient(DB, 27017)
# db = client.sensor_data
# collection = db.sensor_A

class sensor_producer:
    """
    Sensor producer class for different sensors of the monitoring system.
    Ensures scalability and expandabilty of the sensor systems.
    """

    def __init__(self, kafka_topic: str, producer_id: str) -> None:
        self.kafka_topic = kafka_topic
        self.producer_id = producer_id
        self.producer = KafkaProducer(bootstrap_servers=[f'{IP}:9092'],
                                  api_version=(0, 10), 
                                  value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def publish_message(self, data):
        self.producer.send(self.kafka_topic, data)
        print(f"[{self.producer_id}]: {data}")


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Test</p>"

@app.post("/data")
def receive_data():
    sensor_A = sensor_producer("Temp-Dist", "producer_A")
    try:
        data = request.get_json()
        print(data)
        sensor_A.publish_message(data)
        return jsonify({"message": "Data received"}), 200
    except Exception as e:
        print("Error updating database!", e)
        return jsonify({"error": "Bad JSON"}), 400
    

# @app.get("/query")
# def get_data():
#     return_list = []
#     values = list(db.temperature_values.find()) #values: list of dicts
#     for value in values:
#         return_data = {}
#         return_data["Time"] = str(value["Time"])
#         return_data["Temperature"] = str(value["Temperature"])
#         return_list.append(return_data)
#     return jsonify(return_list)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)