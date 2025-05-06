from dotenv import load_dotenv
load_dotenv()  # Loads .env file

import azure.functions as func
import logging, json, requests, openai

# Use environment variables for keys (avoid hardcoding)
import os
openai.api_key = os.environ["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"]
weather_api_key = os.environ["224dda5092d06f673d23b6ced50e5ff6"]

def main(event: func.EventHubEvent):
    try:
        # Decode message (assume small payloads to stay under IoT Hub limits)
        sensor_data = json.loads(event.get_body().decode())
        temp = sensor_data.get('temperature')
        humidity = sensor_data.get('humidity')

        # Call OpenWeatherMap (free tier: 1,000 calls/day)
        weather = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={weather_api_key}"
        ).json()
        condition = weather['weather'][0]['description']

        # Call ChatGPT-3.5-turbo (cheaper than GPT-4)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Cost: $0.002/1k tokens
            messages=[
                {"role": "system", "content": "Suggest outfit and activity in 1 line."},
                {"role": "user", "content": f"{temp}°C, {humidity}% humidity, {condition}. Indoors."}
            ]
        )
        suggestion = response.choices[0].message['content']

        # Send back to Pi via IoT Hub (free tier)
        from azure.iot.hub import IoTHubRegistryManager
        registry_manager = IoTHubRegistryManager(os.environ["IOTHUB_CONN_STR"])
        registry_manager.send_c2d_message("raspberry_pi_id", f"{suggestion}")

    except Exception as e:
        logging.error(f"Error: {str(e)}")