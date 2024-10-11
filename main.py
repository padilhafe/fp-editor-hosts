import json
from app.CriarArquivoHosts import *
from funcs.Constantes import *
from funcs.MenuPrincipal import MenuPrincipal
from funcs.InputDominio import InputDominio

hosts = []
option = 's'

print("""
=======================================================
# Bem vindo a ferramenta de criação de arquivos hosts #
=======================================================
"""
)

while True:
    opcao = MenuPrincipal()
    if opcao == 1:
        with open(CAMINHO_ARQUIVO_HOSTS_GERAL, "r") as file:
            hosts = file.readlines()
            file.close()
        
        if hosts:
            print("Arquivo hosts já existe. O que deseja fazer?\n")
            resposta = int(input("1. Sobrescrever\n2. Adicionar ao final\n3. Exibir conteúdo\n0. Cancelar operação\n > "))
            if resposta == 1:
                modo = "w"
            elif resposta == 2:
                modo = "a"
            elif resposta == 3:
                print("Conteúdo do arquivo hosts:")
                for host in hosts:
                    print(host.strip())
                continue
            elif resposta == 0:
                print("Operação cancelada.\n")
                continue
            else:
                print("Opção inválida! Operação cancelada!\n")
                continue

        with open(CAMINHO_ARQUIVO_SUBDOMINIOS, "r") as file:
            subdominios = json.load(file)
            file.close()

        dominios = InputDominio()
        
        CriarArquivoHosts(CAMINHO_ARQUIVO_HOSTS_GERAL, modo, dominios, subdominios)

    elif opcao == 2:
        print("Qual arquivo deseja editar?")
        
    elif opcao == 3:
        print("falta implementar")
    elif opcao == 4:
        print("falta implementar")
    elif opcao == 5:
        print("falta implementar")
    elif opcao == 0:
        print("Encerrando...")
        exit()
    else:
        print("Opção inválida! Informe novamente.\n")
