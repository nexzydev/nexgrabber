import requests

def test(bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/getChat?chat_id={chat_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('ok') and data.get('result') and data['result'].get('id') == int(chat_id):
            return True
    
    return False
