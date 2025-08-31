import paho.mqtt.client as mqtt
import time
import json
import random

# MQTT broker details
MQTT_BROKER = "mqtt-broker" # From docker-compose.yml
MQTT_PORT = 1883           # Default MQTT port
MQTT_TOPIC = "sensor/data" # Topic to publish dummy data

# Function to generate dummy data
def generate_dummy_data():
    return {
        "test_measurement": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "timestamp": time.time()
    }

# Function to publish dummy data
def publish_dummy_data(client):
    while True:
        dummy_data = generate_dummy_data()
        payload = json.dumps(dummy_data)  # Convert to JSON string
        client.publish(MQTT_TOPIC, payload)
        print(f"Published: {payload} to topic: {MQTT_TOPIC}")
        time.sleep(5)  # Wait for 5 seconds before sending the next message

# Connect to MQTT broker
def main():
    client = mqtt.Client("DummyDataSender")  # Create MQTT client instance
    client.connect(MQTT_BROKER, MQTT_PORT)   # Connect to broker
    print(f"Connected to MQTT broker at {MQTT_BROKER}:{MQTT_PORT}")
    publish_dummy_data(client)

if __name__ == "__main__":
    main()
