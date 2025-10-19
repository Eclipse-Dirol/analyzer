import numpy as np
class Calculations:
    def __init__(self, dict_general):
        self.dict_general = dict_general
        self.dict_words_lengths = self.create_word_lengths(self.dict_general)

    def create_word_lengths(self, dict_words):
        word_length = []
        for sentence in dict_words.values():
            word_length.extend(sentence)
        word_lengths = np.array([len(word) for word in word_length])
        return word_lengths
    
    def sum_letters(self):
        return np.sum(self.dict_words_lengths)
    
    def sum_words(self):
        return len(self.dict_words_lengths)
            
    def words_lengths(self):
        return self.dict_words_lengths
    
    def average_value(self):
        return round(np.mean(self.dict_words_lengths))
    
    def process(self):
        a = self.sum_words()
        b = self.average_value()
        c = self.sum_letters()
        d = self.words_lengths()
        return a,b,c,d