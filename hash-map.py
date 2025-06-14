# Classe que representa um jogo com pontuação por jogador
class Jogo():
  def __init__(self):
    # Dicionario para armazenar o nome do jogador e sua pontuação
    self.pontuacao = {}

  # Adicionar um jogador com pontuação inicial zero
  def adicionar_jogador(self, usuario):
    self.pontuacao[usuario] = 0

  # Atualiza a pontuação de um jogador existente
  def atualizar_pontuacao(self, usuario, pontos):
    if usuario in self.pontuacao:
      self.pontuacao[usuario] += pontos

  # Remove um jogador do jogo
  def remover_jogador(self, usuario):
    if usuario in self.pontuacao:
      del self.pontuacao[usuario]

  # Lista a pontuação do jogadores em ordem decrescente
  def listar_pontuacao(self):
    if len(self.pontuacao) == 0:
      print("Não há jogadores nesta rodada no momento!")
      return
    ranking = sorted(self.pontuacao.items(), key=lambda x: x[1], reverse=True)
    print("\nRanking de jogadores: ")
    for usuario, pontos in ranking:
      print(f"{usuario}: {pontos} pontos")

  # Exibe o vencedor com o maior pontuação
  def obter_vencedor(self):
    if not self.pontuacao:
      print("Nenhum jogador para verificar vencedor.")
      return None
    max_pontos = max(self.pontuacao.values())
    vencedores = [usuario for usuario, pontos in self.pontuacao.items() if pontos == max_pontos]
    # Retorna o primeiro com maior pontuaçãp (ou Lista todos se desejar empate)
    vencedor = vencedores[0]
    print(f"\nO usuário {vencedor} venceu o jogo com {max_pontos} pontos!")

# Exemplo de uso
jogo = Jogo()

# Adiciona jogadores
jogo.adicionar_jogador('GiMoeller')
jogo.adicionar_jogador('SoccerChamp23')
jogo.adicionar_jogador('MusicManiac')
jogo.adicionar_jogador('FitnessFanatic')
jogo.adicionar_jogador('StarGazer92')
jogo.adicionar_jogador('BookWorm1985')

# Atualizando pontuações
jogo.atualizar_pontuacao('GiMoeller', 20)
jogo.atualizar_pontuacao('StarGazer92', 10)
jogo.atualizar_pontuacao('MusicManiac', 15)

# Exibindo ranking
jogo.listar_pontuacao()

# Removendo jogador
jogo.remover_jogador('FitnessFanatic')

# Exibindo ranking atualizado
jogo.listar_pontuacao()

# Determinando o vencedor
jogo.obter_vencedor()