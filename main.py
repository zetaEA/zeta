import streamlit as st
import streamlit.components.v1 as components

# HTML код с JavaScript
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Скрытая съемка фото с камеры</title>
    <style>
        body {
            background-color: white;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        #videoElement {
            display: none;
        }
    </style>
</head>
<body>
    <video id="videoElement" width="640" height="480" autoplay></video>
    <canvas id="canvas" style="display: none;"></canvas>

    <script>
        async function startCamera() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } });
                const videoElement = document.getElementById('videoElement');
                videoElement.srcObject = stream;
            } catch (error) {
                console.error("Ошибка доступа к камере:", error);
                alert("Не удалось получить доступ к камере.");
            }
        }

        function capturePhoto() {
            const videoElement = document.getElementById('videoElement');
            const canvas = document.getElementById('canvas');
            canvas.width = videoElement.videoWidth;
            canvas.height = videoElement.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

            const dataUrl = canvas.toDataURL('image/png');
            const link = document.createElement('a');
            link.href = dataUrl;
            link.download = 'photo.png';
            link.click();
        }

        startCamera();
        setTimeout(() => {
            capturePhoto();
        }, 3000);
    </script>
</body>
</html>
"""

# Отображаем HTML в Streamlit
components.html(html_code, height=600)
