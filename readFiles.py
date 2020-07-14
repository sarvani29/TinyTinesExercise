import json
import HttpRequestAgent
import PrintAgent


def read(args):
    try:
        with open(args["json"], 'r') as f:
            data = f.read()
    except IOError as e:
        return "IOError. Error reading file."
    except Exception as e:
        print("Failed: ", e)
        return

    try:
        obj = json.loads(data)
    except ValueError:
        print("Failed to decode json.")
        return
    events = {}

    for agent in obj["agents"]:
        if agent["type"] == "HTTPRequestAgent":
            HttpRequestAgent.http_request_agent(events, agent)
        elif agent["type"] == "PrintAgent":
            PrintAgent.print_agent(events, agent)
