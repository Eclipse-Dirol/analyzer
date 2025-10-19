import re
class Cleaners:
    def __init__(self, text):
        self.text = text

    def split_sentence(self):
        split_sentence = re.split(r'[!.?;]', self.text)
        split_sentence = [item.strip() for item in split_sentence if item.strip()]
        return split_sentence
    
    def dict_1(self, parts):
        return {i + 1: part for i, part in enumerate(parts) if part}
    
    def template(self, words):
        return {k: v.split() for k, v in words.items()}
    
    def last_template(self, template):
        symbols = '.,!?/#_%$@^&*()"\'{}[];:-_=+'
        return {k: [''.join(ch for ch in word if ch not in symbols) for word in v] 
                for k, v in template.items()}
    
    def process(self):
        parts = self.split_sentence()
        words = self.dict_1(parts)
        temp = self.template(words)
        return self.last_template(temp)


        
        