import requests
import pprint

pp = pprint.PrettyPrinter(indent=4)

state = input("Choose a state! ").upper()

response = requests.get(f"https://api.weather.gov/alerts/active/area/{state}")

response.json()
output = response.json()
output_features = output["features"]
first_feature = output_features[0]
first_properties = first_feature["properties"]

def counties_affected(props):
    area_desc = props["areaDesc"]
    pp.pprint(area_desc)

def event(props):
    event = props["event"]
    pp.pprint(event)

def severity(props):
    severity = props["severity"]
    pp.pprint(severity)

def onset(props):
    onset = props["onset"]
    pp.pprint(onset)

def expires(props):
    expires = props["expires"]
    pp.pprint(expires)

print("BELOW ARE THE AFFECTED SC COUNTIES FOR SEVERE WEATHER AND ALL ALERT DETAILS")
for feature in output_features:
    properties = feature["properties"]
    print("***********************************ALERT***********************************")
    counties_affected(properties)
    event(properties)
    severity(properties)
    onset(properties)
    expires(properties)