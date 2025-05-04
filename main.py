import easyocr
import streamlit as st


def is_string(variable):
    """Check if variable is string."""
    return isinstance(variable, str)


def read_text_from_photo(reader, photo):
    """Extract text from photo using OCR."""
    detection = reader.readtext(photo)
    text = ""
    for row in detection:
        for el in row:
            if is_string(el):
                text += el + "\n"
    return text


def main():
    """Main application function."""
    reader = easyocr.Reader(['ru', 'en'])
    st.title("Загрузка фотографии, с которой вы хотите получить текст")
    st.write("Тестовая ссылка:")
    test_url = "https://static1.wow2print.com/storage/65/gallery/image/1896205816629f8ee1d12786.96956893.webp"  # noqa: E501
    st.write(test_url)

    photo = st.text_input("Вставьте url фотографии")

    if st.button("Обработать") and photo:
        st.image(photo)
        st.title("Вывод текста, считанного с фотографии")
        try:
            text = read_text_from_photo(reader, photo)
            if text:
                st.write("Вывод текста выглядит так:")
                st.write(text)
            else:
                st.write("Нейросети не удалось распознать текст")
        except Exception as e:
            st.error(f"Произошла ошибка: {str(e)}")


if __name__ == "__main__":
    main()
