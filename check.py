# https://telegov.njportal.com/njmvc/CustomerCreateAppointments/GetAvailableDatesForMonth?duration=30&locationId=46&appointmentId=7&date=2022-06-01T04:00:00.000Z
# https://www.twilio.com/blog/5-ways-http-requests-python
import json
import requests

url_template = "https://telegov.njportal.com/njmvc/CustomerCreateAppointments/GetAvailableDatesForMonth?duration=30&locationId={}&appointmentId=7&date=2022-{}-01T04:00:00.000Z"
month = "07"
date_to_beat = 28
locations = {
    "55": "Lodi",
    "47": "Bayonne",
    "263": "Elizabeth",
    "56": "Newark",
    "60": "Rahway",
    "57": "North Bergen",
    "59": "Paterson",
    "67": "Wayne",
    "58": "Oakland",
    "63": "South Plainfield",
    "52": "Edison",
}

def check_availability():
    for key in locations:
        if not key.startswith("__"):
            location = locations[key]
            url = url_template.format(key, month)
            response = requests.get(url)
            json_response = json.loads(response.text)
            if len(json_response) > 0:
                date = json_response[0][8:10]
                if int(date) < date_to_beat:
                    print("{} has appointments!!!".format(location))
                    print("first appointment on {}".format(json_response[0]))
                    print("https://telegov.njportal.com/njmvc/AppointmentWizard/7/{}\n".format(key))


check_availability()
