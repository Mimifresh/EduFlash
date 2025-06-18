import requests
from os import getenv
import re
import json
API_TOKEN = getenv("AI_API_TOKEN")
#API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}


def query(payload):
    response = requests.post(url=API_URL, headers=headers, data=payload)
    return response.json()


instructions = "generate brief and concise question(Q) and answer(A) pair from the text above, do not give further explanations. the questions should be represented by Q: and the answers by A: no extra charaters, avoid numbering."

def main(text):
    text = text.replace('\n', ' ')
    text = text.replace('  ', ' ')
    output = query(json.dumps({
        "model": "deepseek/deepseek-r1-0528:free",
        "messages": [
            {
                "role": "user",
                "content": f"{text}. {instructions}"
            }
        ]
    }))
    output_text = output["choices"][0]["message"]["content"]
    print(output_text)
    questions = re.findall("Q:(.*)\?", output_text)
    answers = re.findall("A:(.*)[.\s]",  output_text)
    dict_ = {}
    for i in range(len(questions)):
        try:
            dict_[questions[i]] = answers[i]
        except Exception:
            pass
    return dict_