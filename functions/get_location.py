import requests
import datetime
import pytz

def get_location():
    # get the public IP address
    ip_request = requests.get('https://api.ipify.org')
    ip_address = ip_request.text

    # pass the IP address to the IP geolocation service
    geo_request_url = f'http://ip-api.com/json/{ip_address}'
    geo_request = requests.get(geo_request_url)
    geo_data = geo_request.json()

    return geo_data

# Pull City and State from ipify's API
location_data = get_location()
location_city = str(location_data["city"])
location_state = str(location_data["region"])

# Get the system's local timezone
local_timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

# Convert the local timezone to its acronym
location_timezone = str(datetime.datetime.now(local_timezone).strftime('%Z'))

acronym_timezone = ''.join(word[0] for word in location_timezone.split())


def get_measurement_system(timezone=acronym_timezone):
    # Define a list of time zones that use the imperial system
    imperial_timezones = ['GMT', 'BST', 'EST', 'EDT']  # Update with the relevant time zones

    # Check if the provided timezone is in the imperial time zones list
    if timezone in imperial_timezones:
        imperial = "imperial"
        return imperial
    else:
        metric = "metric"
        return metric