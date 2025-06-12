# Classe que representa um livro
class Livro:
  def __init__(self, nome, numero_de_paginas):
    self.nome = nome
    self.numero_de_paginas = numero_de_paginas

  def __str__(self):
    return f"{self.nome} ({self.numero_de_paginas} págs)"


# Classe que representa a pilha de livros (estrutura LIFO)
class PilhaDeLivros:
  def __init__(self):
    self.pilha = []

  # Adiciona um novo livro ao topo da pilha
  def adicionar_livro(self, nome, numero_de_paginas):
    novo_livro = Livro(nome, numero_de_paginas)
    self.pilha.append(novo_livro)

  # Remove o livro do topo da pilha
  def remover_livro(self):
    if len(self.pilha) == 0:
      print("A pilha está vazia. Nenhum livro para remover.")
      return None
    return self.pilha.pop()

  # Exibe o livro no topo da pilha sem removê-lo
  def mostrar_livro_topo(self):
    if len(self.pilha) == 0:
      print("A pilha está vazia.")
      return None
    topo = self.pilha[-1]
    print(f"O livro no topo é: {topo}")
    return topo

  # Lista todos os livros na pilha
  def mostrar_livros(self):
    if len(self.pilha) == 0:
      print("Não há livros na pilha no momento!")
      return
    print("Livros na pilha (do fundo ao topo):")
    for livro in self.pilha:
      print(f"  - {livro.nome} ({livro.numero_de_paginas} págs)")


# Exemplo de uso
pilha = PilhaDeLivros()

# Adiciona livros
pilha.adicionar_livro("A Guerra dos Tronos", 600)
pilha.adicionar_livro("A Fúria dos Reis", 648)
pilha.adicionar_livro("A Tormenta das Espadas", 848)
pilha.adicionar_livro("O Festim dos Corvos", 608)
pilha.adicionar_livro("A Dança dos Dragões", 336)

# Mostra todos os livros
pilha.mostrar_livros()

# Remove o topo da pilha
livro_removido = pilha.remover_livro()
if livro_removido:
  print(f"\nLivro removido do topo: {livro_removido.nome} ({livro_removido.numero_de_paginas} págs)")

# Mostra livros restantes
print()
pilha.mostrar_livros()
