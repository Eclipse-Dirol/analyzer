import numpy as np
class Calculations:
    def __init__(self, dict_general):
        self.dict_general = dict_general
        self.dict_words_lengths = self.create_list_word_lengths(self.dict_general)

    def create_list_word_lengths(self, dict_words) -> np.ndarray:
        word_length_list = []
        if len(dict_words.values()) == 0:
            return 0
        else:
            for sentence in dict_words.values():
                word_length_list.extend(sentence)
            word_lengths = np.array([len(word) for word in word_length_list])
            return word_lengths
    
    def sum_letters(self) -> np.ndarray:
        return np.sum(self.dict_words_lengths)
    
    def sum_words(self) -> int:
        value = self.dict_words_lengths
        if isinstance(value, (np.ndarray)):
            return len(value)
        return 0
            
    def words_lengths(self) -> np.ndarray:
        return self.dict_words_lengths
    
    def average_value(self) -> int:
        return round(np.mean(self.dict_words_lengths))
    
    def process(self) -> tuple:
        a = self.sum_words()
        b = self.average_value()
        c = self.sum_letters()
        d = self.words_lengths()
        return a,b,c,d