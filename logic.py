import translate_response


class Translator:
    def __init__(self, source_lang=1, autodetect=True, target_lang=0):
        self.languages = ['ru', 'en', 'fr', 'es', 'it', 'de']
        self.source_lang = self.languages[source_lang]
        self.target_lang = self.languages[target_lang]
        self.autodetect = autodetect

    def translate(self, text):
        if self.autodetect:
            return translate_response.translate_response(text, target=self.target_lang)
        else:
            return translate_response.translate_from_response(text, source=self.source_lang, target=self.target_lang)

    def change_source_lang(self, lang):
        self.source_lang = lang

    def change_target_lang(self, lang):
        self.target_lang = lang

    def change_autodetect(self, autodetect):
        self.autodetect = autodetect
