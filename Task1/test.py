import requests

# ❌ SMELL: Hardcoded Configuration
API_URL = "https://api.open-meteo.com/v1/forecast"

def run_app():
    print("--- Welcome to the Nepal Weather Reporter ---")
    
    # ❌ SMELL: Interactive Loop (Should be CLI arguments)
    while True:
        city = input("\nEnter city name (or 'exit'): ").strip().lower()
        
        if city == 'exit':
            break
            
        # ❌ SMELL: Massive if/elif chain instead of an Enum/Data Structure
        # ❌ SMELL: Hardcoded data logic mixed with UI logic
        if city == "kathmandu":
            lat, lon = 27.7172, 85.3240
        elif city == "pokhara":
            lat, lon = 28.2096, 83.9856
        elif city == "chitwan":
            lat, lon = 27.5291, 84.3542
        elif city == "butwal":
            lat, lon = 27.7006, 83.4484
        elif city == "dhangadi":
            lat, lon = 28.6844, 80.5949
        elif city == "surkhet":
            lat, lon = 28.5997, 81.6358
        elif city == "janakpur":
            lat, lon = 26.7271, 85.9229
        elif city == "jhapa":
            lat, lon = 26.5516, 87.8932
        else:
            # ❌ SMELL: Mixed error handling and UI
            print(f"Error: {city} is not in our licensed regions!")
            continue

        # ❌ SMELL: Network call inside the UI loop (Hard to test)
        query = f"{API_URL}?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(query)
        data = response.json()
        
        # ❌ SMELL: Mathematical logic mixed with printing
        temp_c = data['current_weather']['temperature']
        temp_f = (temp_c * 9/5) + 32
        
        if temp_c > 30:
            status = "HOT"
        elif temp_c < 10:
            status = "COLD"
        else:
            status = "MODERATE"
            
        # ❌ SMELL: Direct printing (Hard to reuse this logic in a web app)
        print(f"--- {city.upper()} ---")
        print(f"Temp: {temp_c}C / {temp_f}F")
        print(f"Condition: {status}")

if __name__ == "__main__":
    run_app()