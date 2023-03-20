import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

state = input("Choose a state to check for severe weather! ").upper()

first_properties = requests.get(f"https://api.weather.gov/alerts/active/area/{state}").json()["features"][0]["properties"]

def counties_affected():
    area_desc = first_properties["areaDesc"]
    pp.pprint(area_desc)

def event():
    event = first_properties["event"]
    pp.pprint(event)

def severity():
    severity = first_properties["severity"]
    pp.pprint(severity)

def onset():
    onset = first_properties["onset"]
    pp.pprint(onset)

def expires():
    expires = first_properties["expires"]
    pp.pprint(expires)

print("BELOW ARE THE AFFECTED SC COUNTIES FOR SEVERE WEATHER AND ALERT DETAILS")
counties_affected()
event()
severity()
onset()
expires()