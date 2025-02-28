import json
import os
import pymysql

def lambda_handler(event, context):
    try:
        # Log the received event
        print("Received event:", json.dumps(event))

        # Extract JSON body if coming from API Gateway
        if "body" in event:
            body = json.loads(event["body"])  # Parse JSON payload
        else:
            body = event  # Direct invocation (e.g., from testing in AWS console)

        local_time = body.get("local_time")
        mode = body.get("mode")
        setpoint = body.get("setpoint")
        hysteresis = body.get("hysteresis")
        relay = body.get("relay") 
        cold_junction = body.get("cold_junction")
        temperature_1 = body.get("temperature_1")
        temperature_2 = body.get("temperature_2")

        # Retrieve DB credentials from environment variables
        DB_HOST = os.getenv('DB_HOST')
        DB_USER = os.getenv('DB_USER') 
        DB_PASSWORD = os.getenv('DB_PASSWORD') 
        DB_NAME = os.getenv('DB_NAME') 

        # Connect to MySQL database
        conn = pymysql.connect(
            host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME
        )
        cursor = conn.cursor()

        # Execute a simple query
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()

        # Close connection
        cursor.close()
        conn.close()

        # Construct response
        response = {
            "statusCode": 200,
            "body": json.dumps(body),
            "local_time": local_time,
            "mode": mode,
            "setpoint": setpoint,
            "hysteresis": hysteresis,
            "relay": relay,
            "cold_junction": cold_junction,
            "temperature_1": temperature_1,
            "temperature_2": temperature_2,
            "db_time": result[0]
        }

    except Exception as e:
        response = {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }

    return response
