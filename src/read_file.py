def filepath(path):
    path = path.replace("\\", "/")
    return path
def read_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()