# README

# BioT's OTP login plugin sample.

When a patient signs up he will automatically change to use CredType OTP and not password.
The plugin configuration should look like below:

{
  "name": "update_credential_type",
  "displayName": "Update to OTP Login",
  "version": 1,
  "runtime": "python3.9",
  "handler": "index.handler",
  "timeout": 10,
  "memorySize": 128,
  "environmentVariables": {},
  "subscriptions": {
    "interceptionOrder": 1,
    "interceptions": [
      {
        "type": "PRE_REQUEST",
        "entityTypeName": "patient",
        "servicePrefix": "/organization",
        "apiId": "POST/organization/v1/users/patients",
        "order": 1
      },
            {
        "type": "PRE_REQUEST",
        "entityTypeName": "patient",
        "servicePrefix": "/organization",
        "apiId": "POST/organization/v1/users/patients/templates/{templateName}",
        "order": 2
      },
            {
        "type": "PRE_REQUEST",
        "entityTypeName": "patient",
        "servicePrefix": "/organization",
        "apiId": "POST/organization/v1/users/patients/sign-up/anonymous",
        "order": 3
      },
            {
        "type": "PRE_REQUEST",
        "entityTypeName": "patient",
        "servicePrefix": "/organization",
        "apiId": "POST/organization/v1/users/patients/sign-up",
        "order": 4
      }
    ],
    "notifications": []
  },
  "enabledState": "ENABLED"
}






