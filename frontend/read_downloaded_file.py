import os

class FileReader:
    def __init__(self, file_path=None, file_type=None):
        self.file_path = file_path
        self.file_type = file_type or self._get_extension(file_path)
        self.supported_types = {'.txt': self._read_txt, '.bin': self._read_unsupported, '.csv': self._read_unsupported}

    def _get_extension(self, file_path):
        if file_path:
            return os.path.splitext(file_path)[1].lower()
        return None

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

    def _read_unsupported(self, uploaded_file):
        raise NotImplementedError("This file type is not currently supported.")