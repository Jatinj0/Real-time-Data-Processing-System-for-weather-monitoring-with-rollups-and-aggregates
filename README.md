# Real-time-Data-Processing-System-for-weather-monitoring-with-rollups-and-aggregates
# Real-Time Weather Monitoring System

## Overview
A Python-based system for real-time weather monitoring that fetches data from the OpenWeatherMap API, processes it, and provides visualizations and alerts for multiple cities.

## Features
- Real-time weather data for multiple cities
- Daily summaries with temperature averages, highs, and lows
- Dominant weather condition identification
- Historical trend visualizations
- Customizable alerts for temperature thresholds (console or email notifications)

## Design Highlights

1. **Modular Architecture**: Separate modules for API, data aggregation, alerts, and visualization enhance maintainability and scalability.

2. **Asynchronous API Calls**: Uses `asyncio` and `aiohttp` for concurrent data retrieval, improving efficiency.

3. **Memory and Database**: Processes recent data in-memory, while historical data is stored in SQLite for long-term analysis.

4. **Configurable Settings**: Customizable parameters (cities, update intervals, alerts) in a centralized configuration file.

5. **Visualization with Matplotlib**: Generates daily and historical weather visualizations.

6. **Flexible Alert System**: Configurable notifications with options for extensions.

## Prerequisites
- Python 3.7+
- pip for installing dependencies

## Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Jatinj0/Real-time-Data-Processing-System-for-weather-monitoring-with-rollups-and-aggregates.git
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**
   - Update API key, cities, update intervals, and alert thresholds in `src/config/config.py`

5. **Run the System**
   ```bash
   python run.py
   ```

## Structure
```plaintext
Real-Time Data Processing System/
├── src/
│   ├── api/
│   ├── data/
│   ├── alerts/
│   ├── visualization/
│   └── config/
├── tests/
├── run.py
└── requirements.txt
```

## Key Configuration Options
- **API_KEY**: OpenWeatherMap API key
- **CITIES**: Cities to monitor
- **UPDATE_INTERVAL**: Interval for updates
- **ALERT_THRESHOLDS**: Temperature alert thresholds

## Running Tests
Run `python -m unittest discover tests` to execute the test suite.

## Customization
- **Add Cities**: Update `CITIES` in `config.py`
- **Adjust Alerts**: Modify `ALERT_THRESHOLDS` in `config.py`
- **Extend Visualizations**: Customize `DataVisualizer` in `visualization/`

## Troubleshooting
- Verify API key and internet connection for data retrieval.
- Ensure Matplotlib is installed for visualizations.
