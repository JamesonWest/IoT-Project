from azure.iot.device import IoTHubDeviceClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get connection string from .env
CONNECTION_STRING = os.getenv("IOTHUB_CONN_STR")

def create_iot_hub_client():
    return IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

print("✅ Connected to Azure IoT Hub!")
