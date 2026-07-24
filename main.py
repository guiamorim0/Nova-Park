from modelos import Estacionamento

estacionamento = Estacionamento()
estacionamento.carregar()

while True:

    print("""
    ===== NOVAPARK - ESTACIONAMENTO =====
    1 - Registrar entrada
    2 - Listar veiculos no patio
    3 - Registrar saida (calcular valor)
    4 - Historico de saidas do dia
    5 - Relatorio
    0 - Sair (salva os dados)\n""")

    opcao = input("Digite uma opcao: ")

    if opcao == "1":
        placa = input("Placa: ").upper()
        modelo = input("Modelo: ")
        if placa == "":
            print("informe a placa!")
        elif not len(placa) == 7:
            print("A placa precisa de 7 caracteres")
        else:
            estacionamento.registrar_entrada(placa, modelo)

    elif opcao == "2":
        estacionamento.listar_patio()

    elif opcao == "3":
        placa = input("Placa: ").upper()
        if not len(placa) == 7:
            print("A placa precisa de 7 caracteres")
        else:
            estacionamento.registrar_saida(placa)

    elif opcao == "4":
        estacionamento.historico_saidas()

    elif opcao == "5":
        estacionamento.relatorio()

    elif opcao == "0":
        estacionamento.salvar()
        print("Saindo...")
        break

    else:
        print("Digite uma opcao valida! (0 - 5)")

    