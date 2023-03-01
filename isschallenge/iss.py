import requests

API = 'http://api.open-notify.org/iss-now.json'

def main():
    response = requests.get(API).json()
    lon= response["iss_position"]["longitude"]
    lat= response["iss_position"]["latitude"]
    print(f"Current location of ISS:\nLon: {lon}\nLat:{lat}")
    
    
if __name__ == "__main__":
    main()
