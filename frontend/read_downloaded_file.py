import pathlib as Path
import pandas as pd

class FileReader:
    def __init__(self, file_type=None):
        self.file_type = file_type
        self.supported_types = {'.txt': self._read_txt, '.bin': self._read_unsupported, '.csv': self._read_csv}

    def read(self, uploaded_file=None):
        if uploaded_file:
            return self.supported_types.get(self.file_type, self._read_unsupported)(uploaded_file)
        raise ValueError("No file provided")

    def _read_txt(self, uploaded_file):
        raw = uploaded_file.read()
        try:
            return raw.decode("utf-8")
        except UnicodeDecodeError:
            return raw.decode("cp1251", errors="replace")
    
    def _read_csv(self, uploaded_file):
        try:
            return pd.read_csv(uploaded_file, index_col=0)
        except Exception as e:
            return e
            
    def _read_unsupported(self, uploaded_file):
        raise NotImplementedError("This file type is not currently supported.")