import time
import json
from azure.connect_iot_hub import IoTHubDeviceClient, create_iot_hub_client
from sensors.temperature_humidity_sensor import read_temp_and_humidity
from sensors.button_input import read_and_send_button_state

def main():
    print("🌐 Connecting to Azure IoT Hub...")
    client = create_iot_hub_client()
    client.connect()
    print("✅ Connected!")

    while True:
        try:
            # Read temperature and humidity
            temperature, humidity = read_temp_and_humidity()
            print(f"🌡️ Temperature: {temperature}°C, 💧 Humidity: {humidity}%")

            # Create and send message for temperature and humidity
            data = {
                "temperature": temperature,
                "humidity": humidity,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }

            print("📤 Sending sensor data to Azure...")
            client.send_message(json.dumps(data))
            print("✅ Sensor data sent!")

            # Read and send button state
            read_and_send_button_state(client)

            # Delay to prevent constant rapid polling
            time.sleep(0.5) 

        except Exception as e:
            print(f"❌ Error in main loop: {e}")

        # Wait before the next loop iteration
        time.sleep(8)
        
if __name__ == "__main__":
    main()
