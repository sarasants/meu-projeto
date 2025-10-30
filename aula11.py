
#pra atualizar
class Carro:
# receber o atributo
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
#exibir algo
    def exibir_informacoes(self):
        return f"Marca: {self.marca}, Ano: {self.ano}, Modelo: {self.modelo}"
        # print (f"marca: {self.marca}, ano:{self.ano}, modelo: {self.modelo}")

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setAno(self, ano):
        self.ano = ano

    def getAno(self):
        return self.ano

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo


# Testando a classe
c1 = Carro('Corolla', 'Toyota', 2020)
print(c1.exibir_informacoes())

c1.setAno(2022)
print(c1.getAno())

    

