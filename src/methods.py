def word_count(last_template):
    return sum(len(last_template[i]) for i in last_template)
def length_words(last_template):
    t = sum(len(i) for d in last_template.values() for i in d)
    w = word_count(last_template)
    return round(t/w)
