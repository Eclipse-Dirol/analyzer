from pathlib import Path
class read_files:
    def __init__(self, filepath):
        self.filepath = filepath

    def return_answer(self):
        return_answer = input()
        filepath = Path(return_answer.replace("\\", "/")).expanduser()
        return filepath
    
    def Try(self, filepath):
        try:
            with filepath.open("r", encoding="utf-8") as f:
                return f.read()
        except:
            return None

    def read_text(self, filepath):
        filepath = Path(filepath)
        while True:
            if filepath.exists() and filepath.is_file():
                return self.Try(filepath)
            else:
                print("File not found, try again, please:")
                f = self.return_answer()
                if f.exists() and f.is_file():
                    return self.Try(f)
    
    def process(self):
        return self.read_text(self.filepath)