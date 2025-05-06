import time
import json
import threading
from azure.connect_iot_hub import create_iot_hub_client
from sensors.temperature_humidity_sensor import read_temp_and_humidity
from sensors.button_input import read_button_state
from azure.upload_to_blob import upload_sensor_data  # <-- your blob uploader

def button_loop(client):
    last_state = None
    while True:
        button_state = read_button_state()
        if button_state != "error" and button_state != last_state:
            print(f"{'✅' if button_state == 'pressed' else '🔘'} Button {button_state.capitalize()}!")

            button_data = {
                "button_state": button_state,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }

            print("📤 Sending button state to Azure...")
            client.send_message(json.dumps(button_data))
            print("✅ Button state sent!")

            last_state = button_state

        time.sleep(0.2)  # Faster polling for responsiveness

def main():
    print("🌐 Connecting to Azure IoT Hub...")
    client = create_iot_hub_client()
    client.connect()
    print("✅ Connected!")

    # Start the button listener in a separate thread
    threading.Thread(target=button_loop, args=(client,), daemon=True).start()

    while True:
        try:
            temperature, humidity = read_temp_and_humidity()
            print(f"🌡️ Temperature: {temperature}°C, 💧 Humidity: {humidity}%")

            outfit_suggestion = "Sweater and jeans"  # Placeholder – later, pull from ChatGPT or logic

            data = {
                "temperature": temperature,
                "humidity": humidity,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }

            print("📤 Sending sensor data to Azure IoT Hub...")
            client.send_message(json.dumps(data))
            print("✅ Sensor data sent!")

            # ⬇ Upload the same data (plus outfit) to Blob Storage
            upload_sensor_data({
                "temperature": temperature,
                "humidity": humidity,
                "outfitSuggestion": outfit_suggestion,
                "time": time.strftime("%Y-%m-%dT%H:%M:%S")
            })
            print("☁️ Sensor data uploaded to Blob Storage.")

        except Exception as e:
            print(f"❌ Error in main loop: {e}")

        time.sleep(8)

if __name__ == "__main__":
    main()