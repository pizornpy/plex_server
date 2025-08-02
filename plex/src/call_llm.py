import requests


def call_llm():


    url = "http://10.255.255.254/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-r1-distill-qwen-7b",
        "messages": [
            {"role": "user", "content": "¿Quien causó el 11s?"}
        ],
        "temperature": 0.7,
        "max_tokens": 512,   # Usa un número positivo
        "stream": False
    }


    response = requests.post(url, headers=headers, json=data)

    result = response.json()
    print(result)

    return result["choices"][0]["message"]["content"]