from pathlib import Path
class read_files:
    def __init__(self, path):
        self.path = path

    def general_input(self):
        i = input()
        return i

    def reworked_path(self):
        path = self.path.replace("\\", "/")
        return path
    
    def return_answer(self):
        return_answer = self.general_input()
        filepath = Path(return_answer.replace("\\", "/")).expanduser()
        return filepath
    
    def read_text(self, filepath):
        filepath = Path(filepath)
        while True:
            if filepath.exists() and filepath.is_file():
                try:
                    with filepath.open("r", encoding="utf-8") as f:
                        return f.read()
                except:
                    print("Error reading file!!!")
                    self.return_answer()
            else:
                print("File not found, try again, please:")
                r = self.return_answer()
                if r.exists() and r.is_file():
                    try:
                        with r.open("r", encoding="utf-8") as f:
                            return f.read()
                    except:
                        exit()
    
    def process(self):
        filepath = self.reworked_path()
        return self.read_text(filepath)





















""" def rework_filepath(path):
    path = path.replace("\\", "/")
    return path
def read_text(filepath):
    while True:
        user_input = input("Введите путь к файлу (или 'q' для выхода):\n").strip()
        if user_input.lower() == 'q':
            print("Выход из программы.")
            return None
        filepath = Path(user_input.replace("\\", "/")).expanduse()
        if filepath.exists() and filepath.is_file():
            try:
                with filepath.open("r", encoding="utf-8") as f:
                    return f.read()
            except:
                print("Error reading file!!!")
        else:
            print("File not found, try again, please")

 """