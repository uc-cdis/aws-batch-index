import os
import sys
import requests
import base64
import json


url = "https://data.bloodpac.org/index/index/"

auth = base64.b64encode("gdcapi: insert your key here".encode())

lineCount = 0

with open("thing.txt", "r") as f:
    file = f.read()
    lines = file.split("\n")
    for line in lines:
        if lineCount % 100 == 0:
            print("hey we have submitted: ", lineCount, "records")

        body = line[:-1]

        response = requests.post(
            url,
            data=body,
            headers={
                "content-type": "application/json",
                "Authorization": "Basic " + auth.decode(),
            },
        )

        code = response.status_code
        if code != 200:
            print("hey there is something wrong with this post")
            print(body)
            print(response.text)
            break
        lineCount += 1
