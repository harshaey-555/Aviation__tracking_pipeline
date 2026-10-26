# ✈️ Live Aviation Tracker

🌍 **Live Application:** [View the Live Flight Tracker Here](https://aviationtrackingpipeline-3ptwkrxsm4bkjgwrvwjvtb.streamlit.app/)

## 📌 Project Overview
The **Live Aviation Tracker** is a real-time data visualization application that monitors and displays live commercial flight data. It interfaces with live aviation APIs to extract, process, and map real-time telemetry data (such as altitude, velocity, and geolocation) for active flights. 

This project demonstrates practical skills in working with external REST APIs, real-time data processing, and building interactive, map-based user interfaces.

## 🚀 Key Features
* **Real-Time Data Extraction:** Fetches live flight telemetry and metadata from [insert API name, e.g., OpenSky Network / AviationStack] via REST API.
* **Interactive Mapping:** Visualizes dynamic flight coordinates on an interactive map.
* **Data Filtering:** Allows users to filter active flights by [insert features, e.g., airline, altitude, or geographic bounding box].
* **Cloud Deployment:** Fully deployed and continuously hosted on [insert platform, e.g., Streamlit Cloud / Render / Vercel].

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Processing:** Pandas, [Requests / JSON]
* **Visualization/UI:** Streamlit, [Folium / Plotly / PyDeck - *keep the one you used*]
* **External API:** [Name of the Flight API you used]

## 💻 Local Execution & Setup

**1. Clone the repository**
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
Create a `.env` file or use `st.secrets` (if using Streamlit) to safely store your API key:
```text
AVIATION_API_KEY=your_api_key_here
```

**5. Run the application**
```bash
streamlit run app.py  # Replace 'app.py' with your actual main file name
```

## 📈 Future Scope
* Implement automated historical flight data archiving using a PostgreSQL database.
* Add predictive analytics for estimated time of arrival (ETA) based on live velocity and distance metrics.

---
*This project was built to demonstrate proficiency in API integration, Data Engineering, and full-stack Python development.*
