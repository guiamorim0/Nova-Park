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
            print("Nenhum veiculo cadastrado!")
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

    def registrar_saida(self, placa: str):
        veiculo = self.buscar_veiculo(placa)
        if veiculo is None:
            print("Nenhum veiculo encontrado!")
            return
        saida = datetime.now()

        diferenca =  saida - veiculo.horario_entrada
        segundos = diferenca.total_seconds()
        horas_cobradas = math.ceil(segundos / 3600)

        if horas_cobradas == 0:
            horas_cobradas = 1

        valor = self.calcular_valor(horas_cobradas)

        print(f"""
        ===== TICKET - {veiculo.placa} =====
        Entrada: {veiculo.horario_entrada.strftime('%H:%M')}
        Saida: {saida.strftime('%H:%M')}
        Permanencia: {horas_cobradas} hora(s) cobrada(s)
        Valor: R$ {valor:.2f}
        """)

        self.saidas.append({
            "placa": veiculo.placa,
            "entrada": veiculo.horario_entrada,
            "saida": saida,
            "valor": valor
            })

        self.patio.remove(veiculo)

    def historico_saidas(self):
        if len(self.saidas) == 0:
            print("Nenhum veiculo encontrado!")
            return
        else:
            for registro in self.saidas:
                print(f"{registro['placa']} | Saida: {registro['saida'].strftime('%H:%M')} | R$ {registro['valor']:.2f}")

    def relatorio(self):
        faturamento = 0
        for registro in self.saidas:
            faturamento += registro['valor']

        print("===== RELATORIO =====")
        print(f"Veiculos no patio: {len(self.patio)}")
        print(f"Total de saidas: {len(self.saidas)}")
        print(f"Faturamento do dia: R$ {faturamento:.2f}")

        if len(self.saidas) > 0:
            ticket_medio = faturamento / len(self.saidas)
            print(f"Ticket medio: R$ {ticket_medio:.2f}")
        else:
            print("Ticket medio: Nenhuma saida registrada")