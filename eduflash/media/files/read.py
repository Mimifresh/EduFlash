#!/usr/bin/python3

import requests
import os
import re
import sys

API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer {}".format(API_KEY)}

file_ = sys.argv[1]
text = ''

with open(file_, 'r') as resource:
    for line in resource:
        text += line
text_array = re.split('.\s', text)


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json
instructions = "The above is a text, generate as much as possible questions and answers and tag it with 'Q' and 'A' respectively"

for sentence in text_array:
    result = query({"inputs": f"{sentence}. {instructions}"})
    print(result)
