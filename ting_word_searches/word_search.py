def add_file_information_to_list(info_list, file, word, include_content):
    info_file = {
        "palavra": word,
        "arquivo": file["nome_do_arquivo"],
        "ocorrencias": list()
    }

    for row_index in range(file["qtd_linhas"]):
        row = file["linhas_do_arquivo"][row_index]
        row_number = row_index + 1

        if word.lower() in row.lower() and include_content:
            info_file["ocorrencias"].append(
                {"linha":  row_number, "conteudo": row}
            )

        elif word.lower() in row.lower():
            info_file["ocorrencias"].append({"linha": row_number})

    if len(info_file["ocorrencias"]):
        info_list.append(info_file)


def create_info_list(word, instance, include_content):
    info_list = list()

    for file_index in range(len(instance)):
        file = instance.search(file_index)
        add_file_information_to_list(info_list, file, word, include_content)

    return info_list


def exists_word(word, instance):
    return create_info_list(word, instance, False)


def search_by_word(word, instance):
    return create_info_list(word, instance, True)
