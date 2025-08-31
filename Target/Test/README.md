# Purpouse

The purpose of this script is to generate fake measurement data to simulate the real device. This allows testing of measurement storage and visualization without the need for hardware or deployment to a remote host. All operations are performed locally on the PC.

The script runs in its own container and sends data via MQTT (over TCP/IP), simulating the behavior of a real device.

# Configuration

Follow [the instructions in this manual](../../Host/README.md) to set up and configure all required containers for this project.

Use the following command to access the test container:

```
docker exec -it hardwaredatalogger-remoteprocessing-hw-mock-1 bash
```

Navigate to the test directory and activate the virtual environment:

```
cd /workspace/Test/
source /workspace/build/venv/bin/activate
```

Execute the test script to start generating random measurement data:

```
python3 test.py
```

The script will simulate data and send it via MQTT. When you no longer need data, stop the script by pressing Ctrl+C.

## Troubleshooting

### Listen for MQTT Messages
Run the following command to listen in the background for messages on the MQTT topic:

```
mosquitto_sub -h mqtt-broker -p 1883 -t "test/topic" &
```

### Send a Test Message

Publish a message to verify the MQTT broker is receiving messages:

```
mosquitto_pub -h mqtt-broker -p 1883 -t "test/topic" -m "Hello, MQTT"
```

### Verify Communication

If the broker is functioning correctly, the message will be echoed back. Example session:

```
(venv) root@fe9a68512386:/workspace/Test# mosquitto_sub -h mqtt-broker -p 1883 -t "test/topic" &
[1] 50
(venv) root@fe9a68512386:/workspace/Test# mosquitto_pub -h mqtt-broker -p 1883 -t "test/topic" -m "Hello, MQTT"
Hello, MQTT
(venv) root@fe9a68512386:/workspace/Test#
```

If any issues persist, ensure the MQTT broker is running and properly configured.
