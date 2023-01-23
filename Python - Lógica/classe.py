# 5. crie pelo menos uma classe e um método
class Carro:
  def __init__(self, modelo, marca, cor, ano):
    self.modelo = modelo
    self.marca = marca
    self.cor = cor
    self.ano = ano

  def descricaoCarro(self):
    print

  def ligarCarro(self, chave=True):
    if chave:
      print("Ligando o carro!")
    else:
      print("Você precisa de sua chave!")

  pass

c1 = Carro("Uno", "Fiat", "Vermelho", "2013")

c1.ligarCarro(True)

# inicio de uma classe
