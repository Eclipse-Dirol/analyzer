import re
class Cleaners:
    def __init__(self, text):
        self.text = text

    def split_sentence(self) -> str:
        split_sentence = self.text.lower()
        split_sentence = re.split(r'[!.?;]', split_sentence)
        split_sentence = [item.strip() for item in split_sentence if item.strip()]
        return split_sentence
    
    def dict_1(self, parts) -> dict:
        return {i + 1: part for i, part in enumerate(parts) if part}
    
    def template(self, words) -> dict:
        return {k: v.split() for k, v in words.items()}
    
    def last_template(self, template) -> dict:
        symbols = '.,!?/#_%$@^&*()"\'{}[];:-_=+'
        clean_template = {}
        for key, words in template.items():
            clean_words = [
                ''.join(ch for ch in word if ch not in symbols)
                for word in words
                ]
            clean_words = [w for w in clean_words if w]
            if clean_words:
                clean_template[key] = clean_words
        return clean_template
    
    def process(self):
        parts = self.split_sentence()
        words = self.dict_1(parts)
        temp = self.template(words)
        return self.last_template(temp)