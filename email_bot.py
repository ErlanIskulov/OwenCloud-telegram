import imaplib
import email
import time
import requests

EMAIL = "owencloudbambino@gmail.com"
PASSWORD = "UZ3812997359"
BOT_TOKEN = "7862986419:AAFrTw9T3PhCaEQMv7zFMUcXYdhhFZlVEjs"
CHAT_ID = "5612157306"

def send_to_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check_email():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")
        result, data = mail.search(None, "(UNSEEN)")
        ids = data[0].split()
        for eid in ids:
            res, mdata = mail.fetch(eid, "(RFC822)")
            msg = email.message_from_bytes(mdata[0][1])
            subject = msg["subject"]
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode(errors="ignore")
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")
            text = f"📬 OwenCloud\n✉ {subject}\n\n📄 {body.strip()[:1000]}"
            send_to_telegram(text)
        mail.logout()
    except Exception as e:
        print("Ошибка:", e)

if __name__ == "__main__":
    while True:
        check_email()
        time.sleep(60)
