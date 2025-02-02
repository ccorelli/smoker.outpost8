import requests
import json
import pi_smoker_secrets

def post_request(url, payload):
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': pi_smoker_secrets.api_key #AWS API Gateway Key  
    }
    
    # Convert payload to JSON format
    json_payload = json.dumps(payload)
    
    try:
        response = requests.post(url, data=json_payload, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Request successful!")
            return response.json()  # Return the response as JSON
        else:
            print(f"Request failed with status code: {response.status_code}")
            return response.text  # Return the raw response text
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

payload = {
    "local_time": "2025-02-01",
    "mode": "off",
    "setpoint": 30,
    "hysteresis": 5, 
    "relay": 1,
    "cold_junction": 30,
    "temperature_1": 100,
    "temperature_2": 101
}
print (post_request(pi_smoker_secrets.submit_smoker_data_api_url, payload))