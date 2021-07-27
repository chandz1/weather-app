import json
import requests


def get_location():
    send_url = (
        "http://api.ipstack.com/check?access_key=6dd029effc540661b332255ceea35c6a"
    )
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    city = geo_json["city"]
    country = geo_json["country_name"]
    return city, country


if __name__ == "__main__":
    print(get_location())
