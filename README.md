# 🅿️ NovaPark — Sistema de Estacionamento

Sistema de console em Python para controle de estacionamento, com cálculo de tarifa por tempo real de permanência e **persistência de dados em arquivo** — os veículos no pátio sobrevivem ao fechamento do programa.

Desenvolvido com Programação Orientada a Objetos, o projeto simula uma demanda real: substituir o controle manual em caderno por um sistema que registra horários automaticamente, calcula valores pela tabela de preço e não perde os dados ao ser fechado.

## ⚙️ Funcionalidades

- Registro de entrada com horário capturado automaticamente (`datetime.now()`)
- Validação de placa (formato e duplicidade no pátio) com normalização para maiúsculas
- Listagem dos veículos atualmente no pátio
- Registro de saída com cálculo de permanência e valor pela tabela de preço
- Histórico das saídas do dia
- Relatório com faturamento e ticket médio
- **Persistência em arquivo:** o pátio é salvo ao sair e recarregado ao iniciar

## 💰 Tabela de preço

- Primeira hora (ou fração): **R$ 15,00**
- Cada hora adicional (ou fração): **R$ 8,00**

Frações de hora são sempre arredondadas para cima (`math.ceil`). Exemplos: 20 minutos → R$ 15,00 | 1h10 → R$ 23,00 | 3h → R$ 31,00.

## 🖥️ Menu do sistema

| Opção | Ação |
|-------|------|
| 1 | Registrar entrada |
| 2 | Listar veículos no pátio |
| 3 | Registrar saída (calcular valor) |
| 4 | Histórico de saídas do dia |
| 5 | Relatório |
| 0 | Sair (salva os dados) |

## 🚀 Como executar

Pré-requisito: Python 3 instalado.

```bash
git clone https://github.com/guiamorim0/novapark.git
cd novapark
python main.py
```

O sistema usa apenas a biblioteca padrão do Python (`datetime` e `math`) — sem dependências externas.

Na primeira execução, um arquivo `patio.txt` é criado automaticamente para persistir os dados. Os veículos que permanecerem no pátio ao sair estarão lá na próxima vez que o programa abrir.

## 📂 Estrutura do projeto

```
novapark/
├── modelos.py   # Classes Veiculo e Estacionamento (lógica, cálculo e persistência)
├── main.py      # Menu interativo e interação com o usuário
├── patio.txt    # Arquivo de persistência (gerado automaticamente)
└── README.md
```

A arquitetura separa a lógica de negócio (`modelos.py`) da interface com o usuário (`main.py`).

## 🧠 Conceitos aplicados

- Programação Orientada a Objetos (classes, `__init__`, `__str__`, métodos de instância)
- Manipulação de data e hora com o módulo `datetime` (`now`, `strftime`, `strptime`, `timedelta`)
- Cálculo de duração a partir da diferença entre dois horários (`total_seconds`)
- Arredondamento de fração para cima com `math.ceil`
- **Persistência em arquivo:** leitura e escrita com `open`, `with`, `write`, `split`
- Tratamento de exceções (`try/except`, `FileNotFoundError`)
- Validação de dados de entrada
- Separação de responsabilidades entre coleta de dados e regras de negócio

## 🏛️ Decisões de arquitetura

- **Cálculo do valor em método separado:** a tarifa é calculada por `calcular_valor(horas)`, isolada da lógica de tempo, o que permite testar a tabela de preço sem depender do relógio.
- **A placa como identificador:** diferente de sistemas com código sequencial, o veículo usa a própria placa como identificador único, já que ela vem do mundo real.
- **Histórico como lista de dicionários:** cada saída é registrada com placa, horários e valor pago, estrutura que mantém os dados legíveis e fáceis de acessar por campo.

## 👤 Autor

**Guilherme Zanchetti Amorim** — Estudante de Engenharia de Software (FIAP)

- GitHub: [github.com/guiamorim0](https://github.com/guiamorim0)
