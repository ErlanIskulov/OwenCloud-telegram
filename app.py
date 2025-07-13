from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7862986419:AAFrTw9T3PhCaEQMv7zFMUcXYdhhFZlVEjs'
CHAT_ID = '5612157306'

@app.route('/')
def home():
    return 'OwenCloud ↔ Telegram OK'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = f"📡 OwenCloud уведомление:\n{data}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)
    return 'OK'
