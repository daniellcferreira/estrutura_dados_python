# Classe que representa um paciente (nó da lista)
class Paciente:
  def __init__(self, id, nome, estado_saude):
    self.id = id
    self.nome = nome
    self.estado_saude = estado_saude
    self.proximo = None   # ponteiro para o proximo paciente na lista

# Classe que representa a lista simples encadeada com ponteiro apenas para o head
class ListaDePacientes:
  def __init__(self):
    self.head = None   # primeiro paciente da lista

  # Adiciona um paciente ao final da lista
  def adicionar_paciente(self, id, nome, estado_saude):
    novo_paciente = Paciente(id, nome, estado_saude)
    if self.head is None:
      # lista vazia: novo paciente se torna a cabeça(head)
      self.head = novo_paciente
    else:
      # percorre até o ultimo nó para adicionar no final
      atual = self.head
      while atual.proximo is not None:
        atual = atual.proximo
      atual.proximo = novo_paciente

  # Remove um paciente com bae no ID
  def remover_paciente(self, id):
    if self.head is None:
      print("Lista vazia. Nenhum paciente para remover.")
      return
    
    if self.head.id == id:
      # paciente a ser removido é a cabeça(head)
      self.head = self.head.proximo
      return
    
    # Busca o paciente na lista
    atual = self.head
    while atual.proximo is not None:
      if atual.proximo.id == id:
        atual.proximo = atual.proximo.proximo
        return
      atual = atual.proximo

  # Lista todos os pacientes
  def listar_pacientes(self):
   if self.head is None:
     print("Não há pacientes nesta lista.")
     return
   
   atual = self.head
   while atual is not None:
    print(f"Nome: {atual.nome}, ID: {atual.id}, Estado de saúde: {atual.estado_saude}")
    atual = atual.proximo

# Exemplo de uso da lista
lista = ListaDePacientes()

# Adiciona pacientes
lista.adicionar_paciente(1, "Danilo", "Estavel")
lista.adicionar_paciente(2, "Carla", "Tratamento intensivo")
lista.adicionar_paciente(3, "Bruno", "Critico")
lista.adicionar_paciente(4, "Bianca", "Estavel")

# Lista pacientes
print("\nLista de pacientes: ")
lista.listar_pacientes()

# Remove um paciente da lista
lista.remover_paciente(3)

# lista novamente após remoção
print("\nLista atualizada: ")
lista.listar_pacientes()