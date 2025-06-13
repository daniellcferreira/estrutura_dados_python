# Classe que representa um produto
class Produto:
  def __init__(self, id, nome, quantidade):
    self.id = id
    self.nome = nome
    self.quantidade = quantidade

# Nó da árvore binária contendo um produto
class Node:
  def __init__(self, produto):
    self.produto = produto
    self.esquerda = None
    self.direita = None

# Estrtura de árvore binária de busca para armazenar produtos
class ArvoveProduto:
  def __init__(self):
    self.raiz = None

  # Metodo publico para inserir um novo produto na árvore
  def inserir_produto(self, id, nome, quantidade):
    novo_produto = Produto(id, nome, quantidade)
    if self.raiz is None:
      self.raiz = Node(novo_produto)
    else:
      self._inserir_produto(novo_produto, self.raiz)

  # Metodo recursivo interno para inserir produto
  def _inserir_produto(self, produto, no_atual):
    if produto.id < no_atual.produto.id:
      if no_atual.esquerda is None:
        no_atual.esquerda = Node(produto)
      else:
        self._inserir_produto(produto, no_atual.esquerda)
    elif produto.id > no_atual.produto.id:
      if no_atual.direita is None:
        no_atual.direita = Node(produto)
      else:
        self._inserir_produto(produto, no_atual.direita)
    else:
      # Atualiza os dados do produto se o ID ja existir
      no_atual.produto = produto

  # Metodo publico para buscar um produto pelo ID
  def buscar_produto(self, id):
    return self._buscar_produto(id, self.raiz)
  
  # Metodo recursivo interno de busca
  def _buscar_produto(self, id, no_atual):
    if no_atual is None or no_atual.produto.id == id:
      return no_atual
    elif id < no_atual.produto.id:
      return self._buscar_produto(id, no_atual.esquerda)
    else:
      return self._buscar_produto(id, no_atual.direita)
    
# Exemplo de uso
arvore = ArvoveProduto()

# Inserindo produtos
arvore.inserir_produto(1, "Camiseta", 10)
arvore.inserir_produto(2, "Vestido", 20)
arvore.inserir_produto(3, "Tenis", 5)

# Buscando produtos existentes 
resultado1 = arvore.buscar_produto(2)
if resultado1:
  print(f"Produto encontrado: {resultado1.produto.nome}")
else:
  print(f"Produto com ID informado não encontrado.")

# Buscando produtos inexistentes
resultado2 = arvore.buscar_produto(20)
if resultado2:
  print(f"Produto encontrado: {resultado2.produto.nome}")
else:
  print("Produto com ID informado não encontrado.")