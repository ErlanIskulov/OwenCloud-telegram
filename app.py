from flask import Flask, request
import requests
import os

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
    requests.post(url, data={'chat_id': CHAT_ID, 'text': message})
    return 'OK'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
