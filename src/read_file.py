from pathlib import Path
class read_files:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        
    def text(self, path):
        path = Path(path)
        if self.examination(path) != False:
            return self.read(path)
        else:
            while True:
                i = Path(input("File not found, try again:\n"))
                f = self.examination(i)
                if f:
                    return self.read(f)
                
    def examination(self, file):
        if file.exists() and file.is_file() == True:
            return file
        else:
            return False
                
    def zero(self, text):
        while len(text) == 0:
            aswer = input("File is empty, try again:\n")
            r = self.text(aswer)
            if r:
                return r
        return text

    def read(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()

    def process(self):
        one = self.text(self.filepath)
        return self.zero(one)
        