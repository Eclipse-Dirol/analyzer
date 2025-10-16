from cleaner import cleaners
from panel import Panel
from read_file import read_files
import methods
def main():
    path = input('Введите путь к файлу:\n')
    read = read_files(path)
    text = read.process()

    c = cleaners(text)
    last_template = c.process()

    word_count = methods.word_count(last_template)
    length_word = methods.length_words(last_template)

    p = Panel(word_count, length_word)
    p.process()
if __name__ == "__main__":
    main()