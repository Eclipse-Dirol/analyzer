def read_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
def split(text):
    return[list_list.strip() for list_list in text.split('.') if list_list.strip()]
def dict_1(parts):
    return {i: part for i, part in enumerate(parts, start=1)}
def template(words):
    return{i: words[i].split() for i in words}
def last_template(template):
    for i in template:
        d = template[i]
        symbols = '.,!?/#_%$@^&*'
        cleaner = [''.join(ch for ch in w if ch not in symbols) for w in d]
        template[i] = cleaner
    return template
def word_count(last_template):
    return sum(len(last_template[i]) for i in last_template)
