import requests
from os import getenv
import re
#API_TOKEN = getenv("HUGGINGFACE_API_TOKEN")
API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


instructions = "generate question as Q: answer as A: pairs from the text above"

def main(text):
    text = text.replace('\n', ' ')
    text = text.replace('  ', ' ')
    output = query({
        'inputs': f"{text}. {instructions}",
        })
    print(output)
    questions = re.findall("\sQ:(.*)\?", output[0]['generated_text'])
    answers = re.findall("\sA:(.*)\.",  output[0]['generated_text'])
    dict_ = {}
    for i in range(len(questions)):
        try:
            dict_[questions[i]] = answers[i]
        except Exception:
            pass
    return dict_