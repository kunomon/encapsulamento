class Jogador:
  # Uma classe jogador com o atributo vida encapsulado
  def __init__(self, nome, vida_inicial=100):
    self.nome = nome
    # O atributo vida é encapsulado usando dois '_' (underscore)
    self.__vida = vida_inicial

  def get_vida(self):
    # Um método público para pegar a vida do jogador
    return self.__vida

  def tomar_dano(self, pontos):
    # Um metodo para retirar a vida do jogador
    self.__vida = max(0, self.__vida - pontos)  # o max garante a vida maior ou igual a 0

# Objeto jogador
jogador1 = Jogador("Samuel")

# Print vida com o uso de encapsulamento
vida_atual = jogador1.get_vida()
print(f"{jogador1.nome} tem {vida_atual} pontos de vida")

# Executa dano
jogador1.tomar_dano(120)
vida_atual = jogador1.get_vida()
print(f"{jogador1.nome} tomou dano e tem {vida_atual} pontos de vida")

# Erro de print vida
print(jogador1.__vida)