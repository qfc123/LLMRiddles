import time
import jwt
import zhipuai
import json  
from .base import register_llm

zhipuai.api_key = "xxxxxxxxx.xxxxxxxx"

def generate_token(apikey: str, exp_seconds: int):
    try:
        id, secret = apikey.split(".")
    except Exception as e:
        raise Exception("invalid apikey", e)

    payload = {
        "api_key": id,
        "exp": int(round(time.time() * 1000)) + exp_seconds * 1000,
        "timestamp": int(round(time.time() * 1000)),
    }

    return jwt.encode(
        payload,
        secret,
        algorithm="HS256",
        headers={"alg": "HS256", "sign_type": "SIGN"},
    )

generate_token(zhipuai.api_key,1)

def ask_chatglm(message: str, api_key: str):
    response = zhipuai.model_api.invoke(
        model="chatglm_turbo",
        prompt=[{"role": "user", "content": message}],
        top_p=0.7,
        temperature=0.9,
    )
    print(response)
    return response['data']['choices'][0]['content'].strip()

register_llm('chatglm', ask_chatglm)
