import utils
from cleaner import cleaners
import пробник
import panel
import read_file
import methods
def main():
    path = input('Введите путь к файлу:\n')
    filepath = read_file.filepath(path)
    text = read_file.read_text(filepath)
    c = cleaners(text)
    parts = c.split()
    words = c.dict_1(parts)
    template = c.template(words)
    last_template = c.last_template(template)
    word_count = methods.word_count(last_template)
    length_word = methods.length_words(last_template)
    panel.show_panel(word_count, length_word)
if __name__ == "__main__":
    main()