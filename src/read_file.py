from pathlib import Path
class read_files:
    def __init__(self, filepath):
        self.filepath = Path(filepath)
        
    def text(self, path):
        path = Path(path)
        if self.examination(path) != False:
            return self.read(path)
        else:
            tries = 1
            while True:
                i = Path(input("File not found, try again:\n"))
                f = self.examination(i)
                if f:
                    return self.read(f)
                if tries == 3:
                    print("Many attempts, try again later.")
                    exit()
                tries +=1
                
    def examination(self, file):
        if file.exists() and file.is_file():
            return file
        else:
            return False
                
    def read(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f'Error: {e}')
            return None

    def zero(self, text):
        attempts = 1
        while not text:
            answer = input("File is empty, try again:\n")
            r = self.text(answer)
            if isinstance(r, str) and r:
                return r
            if attempts==3:
                print("Many attempts, try again later.")
                exit()
            attempts+=1
        return text

    def process(self):
        one = self.text(self.filepath)
        return self.zero(one)
        