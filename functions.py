import easyocr


reader = easyocr.Reader(['en', 'ru'])


def recognize_text_from_image(image_path, reader=reader):
    result = reader.readtext(image_path)
    
    # Объединяем распознанный текст в одну строку
    recognized_text = ' '.join([text[1] for text in result])
    return recognized_text