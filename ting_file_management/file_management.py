import sys


def txt_importer(path_file):
    splited_path_file = path_file.split('.')
    if splited_path_file[-1] != 'txt':
        return sys.stderr.write("Formato inválido\n")

    try:
        with open(path_file, 'r') as file:
            reader = file.read().split("\n")
            return reader
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
