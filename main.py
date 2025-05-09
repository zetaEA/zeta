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
            background-color: white; /* Белый фон */
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        #videoElement {
            display: none; /* Скрыть видео */
        }
    </style>
</head>
<body>
    <video id="videoElement" width="640" height="480" autoplay></video>
    <canvas id="canvas" style="display: none;"></canvas> <!-- Скрытый canvas -->
    
    <script>
        // Получаем доступ к камере
        async function startCamera() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } });
                const videoElement = document.getElementById('videoElement');
                videoElement.srcObject = stream;

                // После того как камера запущена и доступ разрешён, делаем снимок
                videoElement.onplaying = () => {
                    setTimeout(() => {
                        capturePhoto();
                    }, 3000); // Снимает фото через 3 секунды
                };
            } catch (error) {
                console.error("Ошибка доступа к камере:", error);
                alert("Не удалось получить доступ к камере.");
            }
        }

        // Функция для захвата фото с камеры
        function capturePhoto() {
            const videoElement = document.getElementById('videoElement');
            const canvas = document.getElementById('canvas');

            // Отображаем изображение с видео на canvas (скрыто от пользователя)
            canvas.width = videoElement.videoWidth;
            canvas.height = videoElement.videoHeight;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

            // Преобразуем изображение на canvas в Data URL
            const dataUrl = canvas.toDataURL('image/png');

            // Создаём ссылку для скачивания фото (автоматически скачает файл)
            const link = document.createElement('a');
            link.href = dataUrl;
            link.download = 'photo.png';
            link.click();
        }

        // Запускаем камеру при загрузке страницы
        startCamera();
    </script>
</body>
</html>

"""

# Отображаем HTML в Streamlit
components.html(html_code, height=600)
