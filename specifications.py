import re


def interpolate_option(events, option_str):
    bracket_values = [p.split('}}')[0] for p in option_str.split('{{') if '}}' in p]
    if len(bracket_values) > 0:
        conv_values = dot_to_paran(bracket_values)
        option_str = get_conv(conv_values, option_str, events)
    return option_str


def dot_to_paran(paran_values):
    converted_values = []
    for value in paran_values:
        value = value.split(".")
        converted_values.append(value)
    return converted_values


def get_conv(conv_values, option_str, events):
    regex = '\{{[^{]*?\}}'
    for conv_value in conv_values:
        temp = events
        for key in conv_value:
            try:
                temp = temp[key]
            except KeyError as ke:
                print("KeyError ke: ", ke)
                temp = ""
                break
        temp = str(temp)

        option_str = re.sub(regex, temp, option_str, 1)
    return option_str
