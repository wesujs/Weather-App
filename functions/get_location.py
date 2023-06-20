import requests

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
location_state = location_data["region"]