import streamlit as st

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Пример HTML в Streamlit</title>
</head>
<body>
    <h1>Привет, мир!</h1>
    <p>Это сгенерированная HTML-страница внутри Streamlit.</p>
</body>
</html>
"""

# Отображаем HTML-контент в Streamlit
st.markdown(html_content, unsafe_allow_html=True)
