from Televisor import televisor
from ControleRemoto import ControleRemoto

# Criando um televisor
fabricante = input("Digite o fabricante do televisor: ")
modelo = input("Digite o modelo do televisor: ")
televisor = televisor(fabricante, modelo)

# Criando um controle remoto para o televisor
controle = ControleRemoto(televisor)

# Menu de interação com o televisor
while True:
    print("\nMenu:")
    print("1. Aumentar volume")
    print("2. Diminuir volume")
    print("3. Trocar de canal")
    print("4. Sintonizar novo canal")
    print("5. Desligar o televisor")
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == '1':
        valorAumento = int(input("Digite o valor pelo qual deseja aumentar o volume: "))
        controle.aumentaVolume(valorAumento)
    elif opcao == '2':
        valorDiminuicao = int(input("Digite o valor pelo qual deseja diminuir o volume: "))
        controle.diminuiVolume(valorDiminuicao)
    elif opcao == '3':
        canal = input("Digite o canal desejado: ")
        controle.trocaCanal(canal)
    elif opcao == '4':
        canal = input("Digite o nome do novo canal: ")
        controle.sintonizaCanal(canal)
    elif opcao == '5':
        print("Desligando o televisor. Adeus!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")