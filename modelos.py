from datetime import datetime, timedelta

class Veiculo:
    def __init__(self, placa: str, modelo: str):
        self.placa = placa 
        self.modelo = modelo
        self.horario_entrada = datetime.now()

    def __str__(self):
        return f"{self.placa} | {self.modelo} | Entrada: {self.horario_entrada.strftime('%H:%M')}"

veiculo = Veiculo("ABCD123", "Gol")
print(veiculo)


