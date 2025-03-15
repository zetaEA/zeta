import streamlit as st
import random

image_path1 = "1.jpg"
image_path2 = "2.jpg"
image_path3 = "3.jpg"
image_path4 = "4.jpg"
image_path5 = "5.jpg"

st.title("Расписание for IM2")

st.write("Wussup guys!")
st.button("Click me!")
if st.button:
    st.write(random.choice(["Сен кереметсің","Сен лохсың", "Жарадың", "Сұмдықсың"]))
option = st.selectbox("Выберите вариант", ["1.Понедельник", "2.Вторник", "3.Среда", "4.Четверг", "5.Пятница"])

match option:
    case "1.Понедельник":
        st.image(image_path1, caption="Пример изображения", use_container_width=False,width=300)
    case "2.Вторник":
        st.image(image_path2, caption="Пример изображения", use_container_width=False,width=300)
    case "3.Среда":
        st.image(image_path3, caption="Пример изображения", use_container_width=False,width=300)
    case "4.Четверг":
        st.image(image_path4, caption="Пример изображения", use_container_width=False,width=300)
    case "5.Пятница":
        st.image(image_path5, caption="Пример изображения", use_container_width=False,width=300)