# Definindo a classe para representar a lista de compras
class ListaDeCompras:
  def __init__(self):
    self.items = []
    self.quantidades = []

  # Adicionando um novo item à lista de compras
  def adicionar_item(self, item, quantidade):
    self.items.append(item)
    self.quantidades.append(quantidade)

  # Removendo um item da lista de compras
  def remover_item(self, item):
    indexDoItem = self.items.index(item)
    self.items.pop(indexDoItem)
    self.quantidades.pop(indexDoItem)

  # Listando todos os itens da lista de compras
  def listar_itens(self):
    print("Lista de compras: ")
    for i in range(len(self.items)):
      print(f"{self.items[i]}: {self.quantidades[i]}")

listaDeCompras = ListaDeCompras()

listaDeCompras.adicionar_item("caneta", 5)
listaDeCompras.adicionar_item("pen-drive", 3)
listaDeCompras.adicionar_item("caderno", 2)
listaDeCompras.adicionar_item("mochila", 1)

# listaDeCompras.listar_itens()

listaDeCompras.remover_item("mochila")

listaDeCompras.listar_itens()