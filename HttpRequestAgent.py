import json
import requests
from specifications import interpolate_option


def http_request_agent(self, input):
    url = input["options"]["url"]
    url = interpolate_option(self, url)

    try:
        res = requests.get(url)
    except requests.ConnectionError:
        print("failed to connect to url: ", url)
        return
    except Exception as e:
        print("Error in connecting to url")
        return
    try:
        res_text = json.loads(res.text)
    except ValueError:
        print("Failed to decode json.")
        return
    self[input["name"]] = res_text












