from azure.iot.device import IoTHubDeviceClient, Message
import json

# Connection string
conn_str = "HostName=smart-wardrobe-pi-jameson.azure-devices.net;DeviceId=smart-wardrobe-pi;SharedAccessKey=4ca7nrZm56VruR0sZmMqGzkwnEhtQpxcIW4yf5rvw2M="

# Create the IoT Hub client
client = IoTHubDeviceClient.create_from_connection_string(conn_str)
client.connect()

# Dummy JSON message
data = {
    "temperature": 22.5,
    "humidity": 60,
    "weather": "Sunny",
    "suggestion": "Wear a T-shirt and sunglasses."
}
json_message = Message(json.dumps(data))
json_message.content_encoding = "utf-8"
json_message.content_type = "application/json"

# Send the message
client.send_message(json_message)
print("✅ Dummy message sent to Azure IoT Hub!")

# Disconnect
client.disconnect()
