import json
from app.CriarArquivoHosts import *
from funcs.Constantes import *
from funcs.MenuPrincipal import MenuPrincipal
from funcs.InputDominio import InputDominio

hosts = []
option = 's'

print("""
===============================================================================================
# Bem vindo a ferramenta de criação de arquivos hosts da BrasilNET Telecomunicações do Paraná #
===============================================================================================
"""
)

while True:
    opcao = MenuPrincipal()
    if opcao == 1:
        with open(CAMINHO_ARQUIVO_SUBDOMINIOS, "r") as file:
            subdominios = json.load(file)
            file.close()

        dominios = InputDominio()
        
        CriarArquivoHosts(CAMINHO_ARQUIVO_HOSTS_GERAL, dominios, subdominios)

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
