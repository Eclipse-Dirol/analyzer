import utils
import пробник
def main():
    filepath = input('Введите путь к файлу:\n')
    text = utils.read_text(filepath)
    parts =  utils.split(text)
    words = utils.dict_1(parts)
    template = utils.template(words)
    last_template = utils.last_template(template)
    word_count = utils.word_count(last_template)
    length_word = utils.length_words(last_template)
    print(length_word)
if __name__ == "__main__":
    main()
#P:/text_analyzer/data/sample.txt