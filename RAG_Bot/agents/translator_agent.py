from deep_translator import GoogleTranslator
from langdetect import detect

class TranslatorAgent:
    def __init__(self, target_lang: str):
        self.target_lang = target_lang

    def run(self, text: str) -> str:
        src_lang = detect(text)
        return GoogleTranslator(source=src_lang, target=self.target_lang).translate(text)
