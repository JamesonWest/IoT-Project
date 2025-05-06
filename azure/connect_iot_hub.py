from azure.iot.device import IoTHubDeviceClient

# Connection string
CONNECTION_STRING = "HostName=smart-wardrobe-pi-jameson.azure-devices.net;DeviceId=smart-wardrobe-pi;SharedAccessKey=4ca7nrZm56VruR0sZmMqGzkwnEhtQpxcIW4yf5rvw2M="

def create_iot_hub_client():
    return IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("✅ Connected to Azure IoT Hub!")