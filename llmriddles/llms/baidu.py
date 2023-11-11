import requests
import json
from .base import register_llm

API_KEY = 'xxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxx'

url = "https://aip.baidubce.com/oauth/2.0/token"
params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
access_token = str(requests.post(url, params=params).json().get("access_token"))

# 文心大模型 4.0
url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + access_token

headers = {
    'Content-Type': 'application/json'
}

def ask_baidu(message: str, api_key: str):
    payload = json.dumps({
    "messages": [
        {
            "role": "user",
            "content": message
        },
    ]
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    response1 = json.loads(response.text)
    return response1['result']

register_llm('baidu', ask_baidu)

