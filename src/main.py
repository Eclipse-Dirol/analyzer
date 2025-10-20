from cleaner import Cleaners
from panel import Panel
from read_file import Read_Files
from methods import Calculations
def main():
    path = input('Введите путь к файлу:\n')
    read = Read_Files(path)
    text = read.process()

    c = Cleaners(text)
    last_template = c.process()
    
    cal = Calculations(last_template)
    all_calculation = cal.process()

    p = Panel(all_calculation)
    p.process()

if __name__ == "__main__":
    main()