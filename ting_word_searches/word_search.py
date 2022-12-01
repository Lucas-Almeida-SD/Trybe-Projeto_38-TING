def add_file_information_to_list(info_list, file, word):
    info_file = {
        "palavra": word,
        "arquivo": file["nome_do_arquivo"],
        "ocorrencias": list()
    }

    for row_index in range(file["qtd_linhas"]):
        row = file["linhas_do_arquivo"][row_index]

        if word.lower() in row.lower():
            info_file["ocorrencias"].append({"linha":  row_index + 1})

    if len(info_file["ocorrencias"]):
        info_list.append(info_file)


def exists_word(word: str, instance):
    info_list = list()

    for file_index in range(len(instance)):
        file = instance.search(file_index)
        add_file_information_to_list(info_list, file, word)

    return info_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
