import re


def extract_value(param, file_path='.env'):
    # Read the text file
    with open(file_path, "r") as file:
        content = file.read()

    # Split the text into lines
    lines = content.split("\n")

    # Search for the line containing 'model='
    for line in lines:
        if f"{param}=" in line:
            # Extract the value after '='
            model_value = line.split("=")[1].strip()
            return model_value

    # Return None if 'model=' is not found
    return None
