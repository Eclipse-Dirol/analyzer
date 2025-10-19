class Panel:
    def __init__(self, all_calculation):
        self.all_calculation = all_calculation

    def show_panel(self):
        while True:
            self.choice(1)
            try:
                answer_1 = int(input())
            except ValueError:
                print("Wrong format! Try again.")
                continue
            if answer_1 == 1:
                print("answer:", self.all_calculation[0])
            elif answer_1 == 2:
                print("answer:", self.all_calculation[1])
            elif answer_1 == 3:
                print("answer:", self.all_calculation[2])
            elif answer_1 == 4:
                print("answer:", self.all_calculation[3])
            else:
                print("Wrong format!!!")
                continue
            
            self.choice(2)
            try:
                answer_2 = int(input())
            except ValueError:
                print("Wrong format! Try again.")
                continue

            if answer_2 == 1:
                continue
            elif answer_2 == 2:
                print("Okay, bye")
                exit()
            else:
                print("Wrong format!!!")
                exit()

    def choice(self, a):
        if a == 1:
            print("Select action:\n1) Count the number of words.\n2) Calculate the average word length.\n3) Calculate the sum of all letters.\n4) Display the length of all words.")
        elif a == 2:
            print("Do you want to know something else?\n1) YES!\n2) NO!")
    
    def process(self):
        self.show_panel()