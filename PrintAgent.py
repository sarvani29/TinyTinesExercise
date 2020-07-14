from specifications import interpolate_option


def print_agent(self, input):
    message = input["options"]["message"]
    message = interpolate_option(self, message)
    print(message)
    return