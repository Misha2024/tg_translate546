from googletrans import Translator

translator = Translator()


def translate_response(q, target="ru"):
    return translator.translate(q, target).text


def detect_response(q):
    return translator.detect(q).text


def translate_from_response(q, source, target):
    return translator.translate(q, target, source).text
