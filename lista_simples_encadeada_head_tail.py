# Classe que representa um paciente (nó da Lista encadeada)
class Paciente:
  def __init__(self, id, nome, estado_saude):
    self.id = id
    self.nome = nome
    self.estado_saude = estado_saude
    self.proximo = None  # ponteiro para o próximo paciente da lista

# Classe que representa a Lista simples encadeada com ponteiros para head e tail
class ListaDePacientes:
  def __init__(self):
    self.head = None    # primeiro paciente da lista
    self.tail = None    # ultimo paciente da lista

  # Adiciona um novo paciente ao final da lista
  def adicionar_paciente(self, id, nome, estado_saude):
    novo_paciente = Paciente(id, nome, estado_saude)

    if self.head is None:
      # lista vazia: o novo paciente é o primeiro e o último
      self.head = novo_paciente
      self.tail = novo_paciente
    else:
      # lista com elementos: adiciona ao final e atualiza o ponteiro do tail
      self.tail.proximo = novo_paciente
      self.tail =novo_paciente

  # Remove um paciente com base no ID
  def remover_paciente(self, id):
    if self.head is None:
      print("Lista vazia. Nenhum paciente para remover.")
      return
    
    if self.head.id == id:
      # caso o paciente esteja no inicio da lista
      self.head = self.head.proximo
      if self.head is None:
        self.tail = None  # lista ficou vazia

    # Caso o paciente esteja no meio ou no final
    atual = self.head
    while atual.proximo is not None:
      if atual.proximo.id == id:
        atual.proximo = atual.proximo.proximo
        if atual.proximo is None:
          self.tail = atual   # atualiza tail se ultimo for removido
        return
      atual = atual.proximo

  # Lista todos os pacientes na sequência da lista
  def listar_paciente(self):
    if self.head is None:
      print("Não há pacientes nesta lista.")
      return
    
    atual = self.head
    while atual is not None:
      print(f"Nome: {atual.nome}, Id: {atual.id}, Estado de saúde: {atual.estado_saude}")
      atual = atual.proximo

# Exemplo de uso
lista = ListaDePacientes()

# Adiciona pacientes
lista.adicionar_paciente(1, "Giovanna", "Estável")
lista.adicionar_paciente(2, "Lucas", "Tratamento intensivo")
lista.adicionar_paciente(3, "Alex", "Crítico")
lista.adicionar_paciente(4, "Beatriz", "Estável")

# Lista pacientes
print("\nLista de pacientes: ")
lista.listar_paciente()

# Remove um paciente pelo ID
lista.remover_paciente(3)

# Lista novamente após remoção
print("\nLista atualizada: ")
lista.listar_paciente()