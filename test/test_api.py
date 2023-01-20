import base64
import requests
import pprint

file_path = '/Users/mehmetgungoren/Downloads/IMG_8416.JPG'


if __name__ == '__main__':
    url = 'https://mixuwvafi2.execute-api.us-east-2.amazonaws.com/prod/search'

    headers = {}

    data = open(file_path, 'rb').read()  # read bytes from file
    data_base64 = base64.b64encode(data)  # encode to base64 (bytes)
    data_base64 = data_base64.decode()  # convert bytes to string

    data = {
        'image': data_base64,
    }

    response_ai = requests.post(url, headers=headers, json=data)
    response_ai = response_ai.json()
    pprint.pprint(response_ai)
