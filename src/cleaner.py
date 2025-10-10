class cleaners:
    def __init__(self, text):
        self.text = text
    def split(self):
        return[list_list.strip() for list_list in self.text.split('.') if list_list.strip()]
    def dict_1(self, parts):
        return {i: part for i, part in enumerate(parts, start=1)}
    def template(self, words):
        return {i: words[i].split() for i in words}
    def last_template(self, template):
        symbols = '.,!?/#_%$@^&*()"\'\'{}[];:-_=+'
        return {k: [''.join(ch for ch in w if ch not in symbols) for w in v] for k,v in template.items()}
    def process(self):
        parts = self.split()
        words = self.dict_1(parts)
        template = self.template(words)
        return self.last_template(template)