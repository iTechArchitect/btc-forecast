import requests
import json
from datetime import datetime

def get_current_btc_price():
    """Fetch current BTC price from Binance API"""
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(url)
        data = response.json()
        return float(data['price'])
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def generate_forecast():
    """Calculate and generate the 4-hour ahead price forecast"""
    current_price = get_current_btc_price()
    
    if not current_price:
        print("Failed to get current price.")
        return

    predicted_price = round(current_price * 1.0012, 2)
    
    forecast_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "current_btc_price": current_price,
        "forecast_4h_price": predicted_price,
        "status": "success"
    }
    
    with open("forecast_output.json", "w") as f:
        json.dump(forecast_data, f, indent=4)
        
    print(f"Success! Current Price: {current_price}, 4H Forecast: {predicted_price}")

if __name__ == "__main__":
    generate_forecast()