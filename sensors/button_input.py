import time
import grovepi
import json
from azure.connect_iot_hub import IoTHubDeviceClient

# Button connected to port D5
button_port = 5
grovepi.pinMode(button_port, "INPUT")

def read_and_send_button_state(client):
    try:
        button_state = grovepi.digitalRead(button_port)
        if button_state == 1:
            print("✅ Button Pressed!")
        else:
            print("🔘 Button Released!")

        # Create and send message to Azure IoT Hub
        button_data = {
            "button_state": "pressed" if button_state == 1 else "released",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        print("📤 Sending button state to Azure...")
        client.send_message(json.dumps(button_data))
        print("✅ Button state sent!")

    except IOError as e:
        print(f"❌ Error reading button state: {e}")
