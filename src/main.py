from cleaner import cleaners
from panel import Panel
from read_file import read_files
from methods import calculations
def main():
    path = input('Введите путь к файлу:\n')
    read = read_files(path)
    text = read.process()

    c = cleaners(text)
    last_template = c.process()

    cal = calculations(last_template)
    e = cal.process()
    print(e)
    p = Panel(1, 1)
    p.process()
if __name__ == "__main__":
    main()