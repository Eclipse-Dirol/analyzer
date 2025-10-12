import re
class cleaners:
    def __init__(self, text):
        self.text = text

    def split(self):
        return re.split(r'[!.?;.]', self.text)

    def dict_1(self, parts):
        dict_1 = {}
        x=1
        for item in parts:
            dict_1[x] = item
            x+=1
        for key in list(dict_1.keys()):
            if not dict_1[key]:
                del dict_1[key]
        dict_2 = {}
        new_keys=1
        for old_keys in sorted(dict_1.keys()):
            dict_2[new_keys]= dict_1[old_keys]
            new_keys+=1  
        return dict_2

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