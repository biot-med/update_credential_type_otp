# README

# BioT's OTP login plugin sample.

This is a sample code for a pre interceptor plugin that upon patient/caregiver/organization user sign-up, will change it's logon method from a regular password to OTP (One Time Password)


## Prepare package

First we create the virtual environment - Run in command line (use *python/python3* depends on the installation)
```
python3 -m venv seedenv
```
then activate (on Mac)
```
source seedenv/bin/activate
```
(windows)
```
./seedenv/Scripts/activate
```
then run (while the virtual machine is activated) to install all the relevant dependencies 
```
pip install -r requirements.txt 
```

**IMPORTANT** If you add a new dependency while working (pip install), make sure to add the dependency to the requirements.txt file by running  
```
pip freeze > requirements.txt 
```
### Start working

You can add additional logic to the plugin's code -> Go To [src/interceptor_pre/perform.py](./src/interceptor_pre/perform.py) 

run to create plugin.zip file (the pack script and the zip file parts are only relevant for non docker IMAGE plugins, for using the IMAGE deployment package type, scroll down for the docker section)
```
python3 scripts/pack.py
```

Upload the the plugin.zip as with interceptor subscription to any action for any entity as explained [here](https://docs.biot-med.com/docs/custom-lambda-deployment#plugin-api-call)



The plugin configuration for a patient only should look like below (assuming all sign up method are used):

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


For caregivers, the configuration should look like:

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
        "entityTypeName": "caregiver",
        "servicePrefix": "/organization",
        "apiId": "POST/organization/v1/users/caregivers",
        "order": 1
      },
      {
        "entityTypeName": "caregiver",
        "servicePrefix": "/organization",
        "apiId": "POST/organization/v1/users/caregivers/templates/{templateName}",
        "order": 2
      }
    ],
    "notifications": []
  },
  "enabledState": "ENABLED"
}

For organization users, the configuration should look like:

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
        "entityTypeName": "organization-user",
        "servicePrefix": "/organization",
        "apiId": "POST/organization/v1/users/organizations",
        "order": 1
      },
      {
        "entityTypeName": "organization-user",
        "servicePrefix": "/organization",
        "apiId": "POST/organization/v1/users/organizations/templates/{templateName}",
        "order": 2
      }
    ],
    "notifications": []
  },
  "enabledState": "ENABLED"
}


You can configure the plugin to accepts all types of users, or just 2 of them.








