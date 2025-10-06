
""" def word_count(last_template):
    words =0
    for i in last_template:
        x = len(last_template[i])
        words+=int(x)
    return words 
    сокращенно:
    def word_count(last_template):
        return sum(len(last_template[i]) for i in last_template)"""
""" def word_count(template):
    for i in template:
        d = template[i]
        symbols = '.,!?/#_%$@^&*'
        cleaner = [''.join(ch for ch in w if ch not in symbols) for w in d]
        template[i] = cleaner
    return template """
""" def dict_1(parts):
    dict_1 = {}
    x=1
    for list in parts:
        dict_1[x] = list
        x+=1
    return dict_1
     сокращенная:
    def dict_1(parts):
    return {i: part for i, part in enumerate(parts, start=1)}"""
""" def ready_template(words):
    for i in words:
        words[i]=words[i].split()
    return words 
    сокращённая:
    def ready_template(words):
    return{i: words[i].split() for i in words}"""