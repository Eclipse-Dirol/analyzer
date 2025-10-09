import utils
from cleaner import cleaners
import пробник
def main():
    path = input('Введите путь к файлу:\n')
    filepath = utils.filepath(path)
    text = utils.read_text(filepath)
    c = cleaners(text)
    parts = c.split()
    words = c.dict_1(parts)
    template = c.template(words)
    last_template = c.last_template(template)
    word_count = utils.word_count(last_template)
    length_word = utils.length_words(last_template)
    utils.show_panel(word_count, length_word)
if __name__ == "__main__":
    main()