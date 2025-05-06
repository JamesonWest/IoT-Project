from azure.storage.blob import BlobServiceClient
from datetime import datetime
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials from .env
CONNECTION_STRING = os.getenv("AZURE_BLOB_KEY")
container_name = "sensordata"

# Sample sensor data
data = {
    "time": datetime.utcnow().isoformat(),
    "temperature": 25,
    "humidity": 59,
    "outfitSuggestion": "Straight Packets Yo"
}

# Serialize to JSON
file_content = json.dumps(data)
blob_name = f"sensor-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.json"

# Upload to Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

blob_client.upload_blob(file_content, overwrite=True)

print(f"✅ Uploaded {blob_name} to Azure Blob Storage.")
