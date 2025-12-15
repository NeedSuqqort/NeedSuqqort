from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

def fetchData(endpoint, method = "GET", data=None):
    headers = {
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}",
    }
    try:
        response = requests.request(method, endpoint, headers=headers, data=data)
        return response.json()
    except Exception as e:
        print(e)
        return None

def fetch_topX(x = 5):
    return fetchData(f"https://api.spotify.com/v1/me/top/tracks?limit={x}")

with open('res.json','w') as f:
    json.dump(fetch_topX(50), f, indent=4)