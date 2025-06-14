# Estruturas de Dados com Python: Listas, Pilhas, Filas, Árvores e Mapas

![Python](https://img.shields.io/badge/Python-Linguagem-blue?style=flat-square&logo=python)
![Estrutura de Dados](https://img.shields.io/badge/Estrutura%20de%20Dados-Implementa%C3%A7%C3%B5es%20Cl%C3%A1ssicas-orange?style=flat-square)
![CLI](https://img.shields.io/badge/Interface-Terminal-lightgrey?style=flat-square&logo=gnubash)

## Descrição

Este projeto demonstra a implementação prática de estruturas de dados clássicas em Python, com foco didático. Cada estrutura foi aplicada em um exemplo realista, como gerenciamento de pacientes, controle de estoque, organização de livros e sistema de pontuação de jogadores.

O objetivo é consolidar o entendimento de como essas estruturas funcionam internamente, incluindo manipulação de ponteiros, inserção, remoção, busca e ordenação de elementos.

## O que são Estruturas de Dados?

Estruturas de dados são formas organizadas de armazenar, gerenciar e acessar informações de maneira eficiente. Cada tipo de estrutura é ideal para determinados cenários de uso. Neste projeto, foram utilizadas as seguintes:

### Lista Encadeada
Uma sequência de elementos (nós), onde cada nó aponta para o próximo. No caso da lista duplamente encadeada, cada nó também aponta para o anterior. É útil quando há muitas inserções e remoções dinâmicas.

- **Simplesmente Encadeada**: cada nó conhece apenas o próximo.
- **Duplamente Encadeada**: cada nó conhece o próximo e o anterior.

### Pilha (Stack)
Funciona segundo a lógica **LIFO** (Last In, First Out) — o último elemento inserido é o primeiro a ser removido. Imagine uma pilha de livros: só é possível tirar o de cima.

### Árvore Binária de Busca (BST)
Estrutura hierárquica em forma de árvore onde cada nó tem até dois filhos. Os valores menores ficam à esquerda, e os maiores à direita, o que facilita buscas e ordenações.

### Mapa Hash (Hash Map)
Também conhecido como **dicionário**, é uma coleção de pares chave-valor. Permite acesso extremamente rápido a dados com base em uma chave, ideal para contagem, rankings ou buscas diretas.

---

## Funcionalidades

### Lista Simplesmente Encadeada (`lista-simplesmente-encadeada-head.py`)
- Adição de pacientes ao final da lista.
- Remoção de pacientes pelo ID.
- Listagem completa dos pacientes registrados.
- Utiliza apenas o ponteiro `head`.

###  Lista Simplesmente Encadeada com `head` e `tail` (`lista-simplesmente-encadeada-head-tail.py`)
- Otimiza a inserção com o uso de ponteiro `tail`.
- Permite inserção eficiente no final e remoção pelo ID.
- Atualiza corretamente a referência de fim da lista quando necessário.

###  Lista Duplamente Encadeada (`lista-dupla-encadeada.py`)
- Gerenciamento de estoque com produtos interligados nos dois sentidos.
- Remoção de produtos do início, meio ou fim da lista.
- Atualização da quantidade em estoque.
- Listagem completa de produtos com detalhes.

###  Pilha de Livros (`pilhas.py`)
- Adição de livros ao topo da pilha (LIFO).
- Remoção do livro do topo da pilha.
- Visualização do livro atual no topo.
- Impressão de todos os livros empilhados.

### Árvore Binária de Busca (`arvores.py`)
- Inserção ordenada de produtos pela chave `id`.
- Busca eficiente de produtos.
- Atualização dos dados de um produto já existente com base no ID.
- Estrutura ideal para buscas rápidas.

### Hash Map com Dicionário Python (`hash-map.py`)
- Adição e remoção de jogadores.
- Atualização de pontuações de forma eficiente (tempo constante).
- Geração de ranking de jogadores em ordem decrescente.
- Identificação e exibição do jogador vencedor da rodada.

## Tecnologias utilizadas

- **Python 3.10+** — Linguagem de programação utilizada para todas as implementações.
- **Estruturas de Dados Clássicas** — Listas, pilhas, árvores e mapas hash.
- **CLI (Interface de Linha de Comando)** — Execução simples e direta no terminal.

---

Este repositório tem fins educacionais e busca reforçar os conceitos fundamentais de estruturas de dados aplicadas com exemplos claros e contextualizados. Ideal para estudantes e iniciantes em ciência da computação.
