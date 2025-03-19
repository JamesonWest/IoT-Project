# IoT-Powered Smart Wardrobe with AI-Powered Activity Suggestions  

#### 👤 **Student Name:** *James West*  
#### 🆔 **Student ID:** *20098812*  

---

## 📖 1. Introduction  
The **IoT-Powered Smart Wardrobe** is an advanced IoT project that suggests outfits based on:  

- 🌡️ **Real-time weather conditions** (temperature & humidity)  
- 📍 **Location-based weather forecasts**  
- 👕 **User-specific wardrobe data**  
- 🧠 **AI-powered activity & clothing recommendations**  

### 🔗 **Key Components**  
✅ **Sensors** (temperature, humidity, button)  
✅ **Raspberry Pi 4** (processing & cloud connectivity)  
✅ **Azure IoT Hub & Power BI** (data handling & visualization)  
✅ **OpenWeatherMap API & ChatGPT API** (weather and AI-powered insights)  
✅ **OLED Display & RGB LED Strip** (user-friendly visual feedback)  

---

## 🛠️ 2. Proposed Technologies  
### 🔩 **Hardware**  
- **Raspberry Pi 4** – Processing unit for data collection & communication  
- **Grove Sensors:**  
  - 🌡️ **Temperature Sensor** – Monitors ambient temperature  
  - 💦 **Humidity Sensor** – Tracks humidity levels  
  - 🎛️ **Button** – Allows user interaction (e.g., cycle outfit suggestions)  
- **OLED Display** – Displays outfit and activity suggestions  
- **RGB LED Strip** – Provides ambient lighting  

### 💻 **Software**  
- 🐍 **Python** – Handles sensor data, API calls, and cloud integration  
- ☁️ **Azure IoT Hub** – Secure cloud communication  
- 📊 **Power BI** – Visualizes weather & wardrobe data  
- ⚙️ **Azure Functions** – Automates outfit suggestions  
- 🌍 **OpenWeatherMap API** – Fetches weather forecasts  
- 🤖 **ChatGPT API** – Generates AI-powered activity & outfit recommendations  
- 📱 **User Interface (UI)** – Web/mobile app for wardrobe customization  

### 🔗 **Communication Protocols**  
- 📡 **MQTT** – Secure data transmission between Raspberry Pi & Azure IoT Hub  
- 🌐 **HTTP** – Fetches weather & AI-generated suggestions  

---

## 🏛️ 3. IoT Layers  
The project incorporates **four IoT layers**:  

### 🏗️ **1. Sensor Layer**  
- 🌡️ **Temperature Sensor** – Captures real-time temperature  
- 💦 **Humidity Sensor** – Captures real-time humidity  
- 🎛️ **Button** – Allows user interaction  

### 🔄 **2. Processing Node**  
- 🖥️ **Raspberry Pi 4** – Processes sensor data, fetches weather updates, and sends data to the cloud  

### 🌍 **3. Gateway Layer**  
- ☁️ **Azure IoT Hub** – Acts as a gateway for secure cloud communication  

### 🎨 **4. Application Layer**  
- 📊 **Power BI Dashboard** – Visualizes weather, wardrobe, and activity data  
- 🖥️ **OLED Display** – Shows outfit/activity recommendations locally  
- 🌈 **RGB LED Strip** – Provides ambient lighting based on outfit themes  
- 🤖 **ChatGPT API** – Generates AI-powered suggestions  
- 📱 **User Interface** – Allows users to input wardrobe items & refine suggestions  

---

## 🏗️ 4. Design  
### 📌 **System Architecture**  
- **Sensors** → Raspberry Pi collects data  
- **Weather Forecasts** → Retrieved via OpenWeatherMap API  
- **Processing** → Data sent to Azure IoT Hub via MQTT  
- **AI Suggestions** → ChatGPT API generates activities & outfits  
- **User Interaction** → UI allows wardrobe customization  
- **Display & Actuation** → OLED & RGB LED provide real-time feedback  

### 🔄 **Flowchart**  
**Sensor Data** → **Raspberry Pi** → **Fetch Weather Data** → **Azure IoT Hub** → **Power BI/Azure Functions** → **ChatGPT API** → **OLED Display/RGB LED**  

**User Wardrobe Input** → **User Interface** → **ChatGPT API** → **Refined Suggestions** → **OLED Display**  

---

## 🚀 5. Implementation  

### 📡 **1. Sensor Data Collection**  
- Use **Python** to read data from **temperature sensor, humidity sensor, and button**  
- Timestamp & store data locally on **Raspberry Pi**  

### 🌍 **2. Weather Forecast Integration**  
- Fetch weather forecasts via **OpenWeatherMap API**  
- Retrieve **temperature, humidity, and weather conditions (e.g., rain, snow, etc.)**  

### 📤 **3. Telemetry Transmission**  
- Send **JSON-formatted sensor & weather data** to **Azure IoT Hub (via MQTT)**  
- Implement **error handling & retry mechanisms**  

### 📊 **4. Data Visualization**  
- Use **Power BI** to visualize **temperature, humidity, weather forecasts, and outfit suggestions**  

### 🧠 **5. AI-Powered Activity Recommendations**  
- Use **ChatGPT API** to generate **activity recommendations** based on weather:  
  - 🌧️ **Rainy** → Indoor activities (e.g., museums, cafés)  
  - ☀️ **Sunny** → Outdoor activities (e.g., hiking, beach trips)  
- Suggest **appropriate clothing** based on activity type  

### 👕 **6. User-Specific Wardrobe Input**  
- Develop a **web/mobile app** for users to input wardrobe items (e.g., shirts, pants, jackets)  
- Store this data in a **local database or Azure Blob Storage**  

### 🔄 **7. Iterative Suggestions**  
- Users can **refine suggestions** (e.g., *"I need something more formal"*)  
- **ChatGPT API** generates refined outfit/activity recommendations  

### ⚙️ **8. Data Processing & Actuation**  
- **Azure Functions** analyze **temperature, humidity, and weather data**  
- **RGB LED strip** adapts lighting based on outfit themes  

### 🖥️ **9. Local Feedback**  
- **OLED Display** showcases outfit & activity suggestions  
- **RGB LED Strip** provides ambient lighting for a visually enhanced experience  
