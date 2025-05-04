

from functions import recognize_text_from_image


def test_recognizing_text():

    input_data = "https://bsd-group.ru/wp-content/uploads/%D0%BC%D1%8B2.png"

    expected_output = "МЫ ОТКРЫЛИСЬ"

    assert recognize_text_from_image(input_data) == expected_output
