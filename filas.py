# Classe que representa um pedido feito pelo cliente
class Pedido:
  def __init__(self, numero, nome, prato):
    self.numero = numero
    self.nome = nome
    self.prato = prato

# Classe que simula uma fila de pedidos usando uma lista
class FilaPedidos:
  def __init__(self):
    self.fila_pedidos = []  # lista que representa a fila

  # Adiciona um novo pedido ao final da fila
  def adicionar_pedido(self, numero, nome, prato):
    novo_pedido = Pedido(numero, nome, prato)
    self.fila_pedidos.append(novo_pedido)    # Fila: entrada no final (FIFO)

  # Remove o primeiro pedido da fila (o que está há mais tempo esperando)
  def remover_pedido(self):
    if len(self.fila_pedidos) == 0:
      print("Fila vazia! Nenhum pedido para atender.")
      return None
    return self.fila_pedidos.pop(0)   # Fila: saida no inicio

  # Exibe todos os pedidos ainda na fila
  def mostrar_pedidos(self):
    if len(self.fila_pedidos) == 0:
      print("Não ha pedidos no momento!")
      return
    print("Pedidos na fila:")
    for pedido in self.fila_pedidos:
      print(f"Número: {pedido.numero}, Nome: {pedido.nome}, Prato: {pedido.prato}") 

# Exemplo de uso da fila de pedidos
fila = FilaPedidos()

# Adicionando pedidos
fila.adicionar_pedido(1, "João", "Hamburguer")
fila.adicionar_pedido(2, "Maria", "Pizza")
fila.adicionar_pedido(3, "José", "Sushi")

# Mostrando pedidos antes de atender
fila.mostrar_pedidos()

# Removendo o primeiro pedido da fila
pedido_atendido = fila.remover_pedido()
if pedido_atendido:
  print(f"\nPedido atendido: Numero {pedido_atendido.numero}, Prato: {pedido_atendido.prato}\n")

# Mostrando pedidos restantes
fila.mostrar_pedidos()