class Panel:
    def __init__(self, word_count, length_word):
        self.word_count = word_count
        self.length_word = length_word

    def show_panel(self):
        while True:
            self.choice(1)
            try:
                answer = int(input())
            except ValueError:
                print("Wrong format! Try again.")
                continue

            if answer == 1:
                print("answer:", self.word_count)
            elif answer == 2:
                print("answer:", self.length_word)
            else:
                print("Wrong format!!!")
                exit()

            self.choice(2)
            try:
                answer_2 = int(input())
            except ValueError:
                print("Wrong format! Try again.")
                continue

            if answer_2 == 1:
                continue
            elif answer_2 == 2:
                print("Okey, bye")
                exit()
            else:
                print("Wrong format!!!")
                exit()

    def choice(self, a):
        if a == 1:
            print("Select action:\n1) Count the number of words.\n2) Calculate the average word length.")

        elif a == 2:
            print("Do you want to know something else?\n1) YES!\n2) NO!")
    
    def process(self):
        return self.show_panel()