# Classe que representa um produto no estoque
class Produto:
  def __init__(self, codigo_barras, nome, preco, quantidade):
    self.codigo_barras = codigo_barras
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade
    self.proximo_produto = None
    self.produto_anterior = None

# Classe que representa a lista duplamente encadeada de produtos
class ListaDeProdutos:
  def __init__(self):
    self.head = None
    self.tail = None

  # Adiciona um novo produto ao final da lista
  def adicionar_produto(self, codigo_barras, nome, preco, quantidade):
    novo_produto = Produto(codigo_barras, nome, preco, quantidade)
    if self.head is None:
      self.head = novo_produto
      self.tail = novo_produto
    else:
      self.tail.proximo_produto = novo_produto
      novo_produto.produto_anterior = self.tail
      self.tail = novo_produto

  # Remove um produto da lista com base no código de barras
  def remover_produto(self, codigo_barras):
    if self.head is None:
      return
    # Remove da cabeça
    if self.head.codigo_barras == codigo_barras:
      self.head = self.head.proximo_produto
      if self.head is not None:
        self.head.produto_anterior = None
      else:
        self.tail = None
      return
    # Remove da cauda
    if self.tail.codigo_barras == codigo_barras:
      self.tail = self.tail.produto_anterior
      if self.tail is not None:
        self.tail.proximo_produto = None
      return
    # Remove do meio
    produto_atual = self.head
    while produto_atual is not None:
      if produto_atual.codigo_barras == codigo_barras:
        if produto_atual.produto_anterior is not None:
          produto_atual.produto_anterior.proximo_produto = produto_atual.proximo_produto
        if produto_atual.proximo_produto is not None:
          produto_atual.proximo_produto.produto_anterior = produto_atual.produto_anterior
        return
      produto_atual = produto_atual.proximo_produto

  # Atualiza a quantidade em estoque de um produto específico
  def atualizar_quantidade(self, codigo_barras, nova_quantidade):
    produto_atual = self.head
    while produto_atual is not None:
      if produto_atual.codigo_barras == codigo_barras:
        produto_atual.quantidade = nova_quantidade
        return
      produto_atual = produto_atual.proximo_produto

  # Exibe todos os produtos no estoque
  def listar_produtos(self):
    if self.head is None:
      print("Não há produtos no estoque.")
    else:
      produto_atual = self.head
      while produto_atual is not None:
        print(f"Código de barras: {produto_atual.codigo_barras}, Nome: {produto_atual.nome}, Preço: R${produto_atual.preco:.2f}, Quantidade: {produto_atual.quantidade}")
        produto_atual = produto_atual.proximo_produto


# Exemplo de uso
lista_de_produtos = ListaDeProdutos()

# Adicionando produtos
lista_de_produtos.adicionar_produto("001", "Arroz", 10.50, 50)
lista_de_produtos.adicionar_produto("002", "Feijão", 8.90, 30)
lista_de_produtos.adicionar_produto("003", "Macarrão", 5.99, 70)
lista_de_produtos.adicionar_produto("004", "Óleo", 7.50, 20)

# Listando produtos
lista_de_produtos.listar_produtos()

# Atualizando quantidade do Arroz
lista_de_produtos.atualizar_quantidade("001", 40)

# Listando novamente após atualização
print("\n")
lista_de_produtos.listar_produtos()

# Removendo o produto "Macarrão"
lista_de_produtos.remover_produto("003")

# Listando após remoção
print("\n")
lista_de_produtos.listar_produtos()
