import streamlit as st
import pandas as pd
import os

# Файл для сохранения разметки
MARKUP_FILE = "markup.csv"

# Загрузка данных
def load_data():
    if os.path.exists(MARKUP_FILE):
        return pd.read_csv(MARKUP_FILE)
    else:
        return pd.DataFrame(columns=["data", "label"])

# Сохранение разметки
def save_data(dataframe):
    dataframe.to_csv(MARKUP_FILE, index=False)

# Оглавление
st.title("Разметка данных для ML")

# Загружаем данные
markup = load_data()

new_data = st.text_area("Введите текст для разметки:")

# Выбор метки
label = st.selectbox("Выберите метку:", ["Царь", "Виталий", "Березин"])

# Кнопка для сохранения
if st.button("Сохранить разметку"):
    if new_data:
        # Создаем новую строку данных
        new_row = pd.DataFrame({"data": [new_data], "label": [label]})
        markup = pd.concat([markup, new_row], ignore_index=True)
        
        # Сохраняем обновленные данные
        save_data(markup)
        st.success("Данные сохранены!")
    else:
        st.error("Введите текст для разметки!")

st.subheader("Сохраненные данные")
st.write(markup)
