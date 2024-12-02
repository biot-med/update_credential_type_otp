import json

# This function will modify the request JSON data and send it back to complete the call.

def update_credential_type(data: dict):
    # Access the body of the request
    body_data = data["body"]["request"]["body"]

    # Add "_credentialType" with value "OTP"
    body_data["_credentialType"] = "OTP"

    # Construct and return the updated response
    return json.dumps({
        "request": {
            "path": data["body"]["request"]["path"],
            "queryParameters": data["body"]["request"]["queryParameters"],
            "headers": data["body"]["request"]["headers"],
            "body": body_data
        }
    })