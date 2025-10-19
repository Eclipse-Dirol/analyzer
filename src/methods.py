import numpy as np
class calculations:
    def __init__(self, dict_general):
        self.dict_general = dict_general
        self.dict_words_lengths = self.list_np(self.dict_general)

    def list_np(self, dict_words):
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
        self.sum_letters()
        self.sum_words()
        self.words_lengths()
        self.average_value()