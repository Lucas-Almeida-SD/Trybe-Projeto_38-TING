# Projeto TING (Trybe Is Not Google)

Esse projeto foi realizado para exercitar o que foi aprendido na Seção 5 do Módulo de Ciência da Computação do curso da [Trybe](https://www.betrybe.com/), no qual foi sobre `Arrays`, `Nó e Listas Encadeadas` e `Pilhas e Filas`.

Neste projeto foi implementado um programa que simule um algoritmo de indexação de documentos similar ao do `Google`. O programa é capaz de identificar ocorrências de termos em arquivos `TXT`.

O programa desenvolvido possui dois módulos:

- __Módulo de gerenciamento de arquivos__ que permite anexar arquivos de texto (formato TXT) e;

- __Módulo de buscas__ que permite operar funções de busca sobre os arquivos anexados..

## Tecnologias

  - Python

## Como executar

Clone o projeto e acesse a pasta do mesmo.

```bash
$ git clone git@github.com:Lucas-Almeida-SD/Trybe-Projeto_38-TING.git

$ cd Trybe-Projeto_38-TING
```

Para iniciá-lo, siga os passos abaixo:

```bash
# criar e ativar o ambiente virtual
$ python3 -m venv .venv && source .venv/bin/activate

# instalar as dependências no ambiente virtual
$ python3 -m pip install -r dev-requirements.txt
```

O módulo de gerenciamento de arquivos e o módulo de busca estão nos diretórios `ting_file_management` e `ting_word_searches`, respectivamente.