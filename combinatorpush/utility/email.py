import requests

def send_email(content, env_data):

    headers = {
        'X-MAGICBELL-API-KEY': env_data.magicbell_api_key,
        'X-MAGICBELL-API-SECRET': env_data.magicbell_api_secret,
    }

    data = {
        "notification": {
            "title": "Welcome to MagicBell",
            "content": content,
            "category": "new_message",
            "recipients": [
                {"email": env_data.to_email}
            ],
        }
    }

    response = requests.post('https://api.magicbell.com/notifications', headers=headers, json=data)