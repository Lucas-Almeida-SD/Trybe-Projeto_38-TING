def add_file_information_to_list(
    info_list,
    file_name,
    row,
    row_number,
    word,
    include_content
):
    if not len(info_list) or info_list[-1]["arquivo"] != file_name:
        info_list.append({
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": list()
        })

    info_list[-1]["ocorrencias"].append({"linha": row_number})

    if include_content:
        info_list[-1]["ocorrencias"][-1].update({"conteudo": row})


def create_unstructured_files_list(instance):
    unstructured_files_list = list()

    for file_index in range(len(instance)):
        file = instance.search(file_index)
        file_info = [file["nome_do_arquivo"]] * file["qtd_linhas"]
        file_zip = list(zip(file_info, file["linhas_do_arquivo"]))
        unstructured_files_list.extend(file_zip)

    return unstructured_files_list


def create_info_list(word, instance, include_content):
    unstructured_files_list = create_unstructured_files_list(instance)
    file_name, row, row_num = '', '', 0
    info_list = list()

    for file in unstructured_files_list:
        if file[0] != file_name:
            file_name = file[0]
            row_num = 0

        row = file[1]
        row_num += 1

        if word.lower() in row.lower():
            add_file_information_to_list(
                info_list, file_name, row, row_num, word, include_content
            )

    return info_list


def exists_word(word, instance):
    return create_info_list(word, instance, False)


def search_by_word(word, instance):
    return create_info_list(word, instance, True)
