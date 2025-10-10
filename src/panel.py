def show_panel(word_count, length_word):
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
                exit()
def choice(a):
    if a == 1:
        answer_1 = print("Select action:\n1) Count the number of words.\n2) Calculate the average word length.")
    elif a == 2:
        answer_2 = print("Do you want to know something else?\n1) YES!\n2) NO!")