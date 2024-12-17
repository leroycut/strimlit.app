import streamlit as st
import pandas as pd
import os

# Файл для сохранения разметки
ANNOTATION_FILE = "annotations.csv"

# Загрузка данных
def load_data():
    if os.path.exists(ANNOTATION_FILE):
        return pd.read_csv(ANNOTATION_FILE)
    else:
        return pd.DataFrame(columns=["data", "label"])

# Сохранение разметки
def save_data(dataframe):
    dataframe.to_csv(ANNOTATION_FILE, index=False)

# Интерфейс Streamlit
st.title("Разметка данных для ML")

# Загружаем данные
annotations = load_data()

# Поле для ввода нового текста
new_data = st.text_area("Введите текст для разметки:")

# Выбор метки
label = st.selectbox("Выберите метку:", ["Позитив", "Негатив", "Нейтрально"])

# Кнопка для сохранения
if st.button("Сохранить разметку"):
    if new_data:
        # Создаем новую строку данных
        new_row = pd.DataFrame({"data": [new_data], "label": [label]})
        
        # Добавляем новую строку к DataFrame с помощью concat
        annotations = pd.concat([annotations, new_row], ignore_index=True)
        
        # Сохраняем обновленные данные
        save_data(annotations)
        st.success("Данные сохранены!")
    else:
        st.error("Введите текст для разметки!")

# Вывод сохраненных данных
st.subheader("Сохраненные данные")
st.write(annotations)
