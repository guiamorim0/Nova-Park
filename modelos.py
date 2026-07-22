from datetime import datetime, timedelta
import math

class Veiculo:
    def __init__(self, placa: str, modelo: str):
        self.placa = placa 
        self.modelo = modelo
        self.horario_entrada = datetime.now()

    def __str__(self):
        return f"{self.placa} | {self.modelo} | Entrada: {self.horario_entrada.strftime('%H:%M')}"

veiculo = Veiculo("ABCD123", "Gol")
print(veiculo)

class Estacionamento:
    def __init__(self):
        self.patio = []
        self.saidas = []

    def registrar_entrada(self, placa: str, modelo: str):
        for veiculo in self.patio:
            if veiculo.placa == placa:
                print("A placa desse veiculo ja foi cadastrada!")
                return

        novo_veiculo = Veiculo(placa, modelo)

        self.patio.append(novo_veiculo)
        print(f"Veiculo {placa} registrado as {novo_veiculo.horario_entrada.strftime('%H:%M')}! ")

    def listar_patio(self):
        if len(self.patio) == 0:
            print("Nenhum carro cadastrado!")
            return
        for veiculo in self.patio:
            print(veiculo)

    def buscar_veiculo(self, placa: str):
        veiculo_encontrado = None
        for veiculo in self.patio:
            if veiculo.placa == placa:
                veiculo_encontrado = veiculo
                break
        return veiculo_encontrado

    def calcular_valor(self, horas: int):
        preco_fixo = 15
        horas_adicionais = horas - 1
        preco_adicional = horas_adicionais * 8
        return preco_fixo + preco_adicional