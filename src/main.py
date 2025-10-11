from cleaner import cleaners
from panel import show_panel
from read_file import read_files
import methods
def main():
    path = input('Введите путь к файлу:\n')
    read = read_files(path)
    text = read.process()
    print(text)
    c = cleaners(text)
    last_template = c.process()

    word_count = methods.word_count(last_template)
    length_word = methods.length_words(last_template)
    show_panel(word_count, length_word)
if __name__ == "__main__":
    main()
#P:\text_analyzer\src\data\sample.txt