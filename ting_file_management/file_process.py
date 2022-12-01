from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(data)
    sys.stdout.write(f"{data}")


def remove(instance):
    if not len(instance):
        return sys.stdout.write("Não há elementos\n")

    removed_file = instance.search(0)
    removed_file_name = removed_file["nome_do_arquivo"]

    instance.dequeue

    sys.stdout.write(
        f"Arquivo {removed_file_name} removido com sucesso\n"
    )


def file_metadata(instance, position):
    try:
        get_file_data = instance.search(position)
        sys.stdout.write(f"{get_file_data}")
    except IndexError:
        sys.stderr.write("Posição inválida")
