""" def show_panel(word_count, length_word):
    choice(1)
    while True:
        answer = int(input())
        if answer == 1:
            print("answer:", word_count)
            choice(2)
            answer_2 = int(input())
            if answer_2 == 1:
                return show_panel(word_count, length_word)
            elif answer_2 == 2:
                print("Okey, bye")
                exit()
            else:
                print("Wrong format!!!")
                exit()
        elif answer == 2:
            print("answer:", length_word)
            choice(2)
            answer_2 = int(input())
            if answer_2 == 1:
                return show_panel(word_count, length_word)
            elif answer_2 == 2:
                print("Okey, bye")
                exit() 
            else:
                print("Wrong format!!!")
                exit() """
""" def choice(a):
    if a == 1:
        answer_1 = print("Select action:\n1) Count the number of words.\n2) Calculate the average word length.")
        return answer_1
    elif a == 2:
        answer_2 = print("Do you want to know something else?\n1) YES!\n2) NO!")
        return answer_2  """
""" def length_word(last_template):
    t=0
    y=0
    for i in last_template:
        d = last_template[i]
        for item in d:
            t+=len(item)
    w=word_count(last_template)
    y=t/w
    print(round(y))
    сокращенно:
def length_word(last_template):
    t = sum(len(i) for d in last_template.values() for i in d)
    w = word_count(last_template)
    return round(t/w)"""
""" def word_count(last_template):
    words =0
    for i in last_template:
        x = len(last_template[i])
        words+=int(x)
    return words 
    сокращенно:
def word_count(last_template):
    return sum(len(last_template[i]) for i in last_template)"""
""" def last_template(template):
    for i in template:
        d = template[i]
        symbols = '.,!?/#_%$@^&*'
        cleaner = [''.join(ch for ch in w if ch not in symbols) for w in d]
        template[i] = cleaner
    return template 
    сокращённо:
    def last_template(template):
        symbols = '.,!?/#_%$@^&*()'
        return {k: [''.join(ch for ch in w if ch not in symbols) for w in v] for k,v in template.items()}"""
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