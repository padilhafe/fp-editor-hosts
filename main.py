import json
import os
from dotenv import load_dotenv
from app.CriarArquivoHosts import *
from funcs.Constantes import *
from funcs.MenuPrincipal import MenuPrincipal
from funcs.MenuArquivos import MenuArquivos
from funcs.InputDominio import InputDominio

# Instanciação de variáveis globais
hosts_files = {}

# Tenta carregar variáveis de ambiente do arquivo .env para dentro da variável hosts_files
try:
    load_dotenv(override=True, dotenv_path=".env")
except FileNotFoundError:
    print(f"Arquivo .env não encontrado. Por favor, crie um arquivo.env com as configurações necessárias (consulte o arquivo readme.md para mais detalhes).")
    exit(1)

try:
    for environment_variable in os.environ:
        if "DIR_HOSTS" in environment_variable:
            hosts_files[environment_variable.replace("DIR_HOSTS_", "").lower()] = os.environ[environment_variable]
except KeyError as e:
    print(f"Variável de ambiente '{e}' não encontrada.")
    exit(1)

print(f"""
=======================================================
# Bem vindo a ferramenta de criação de arquivos hosts #
=======================================================
"""
)

while True:
    opcao = MenuPrincipal()
    if opcao == 1:
        caminho = MenuArquivos(hosts_files)

        if type(caminho) is str:
            try:
                with open(caminho, "r") as file:
                    hosts = file.readlines()
                    file.close()
            
            except FileNotFoundError:
                hosts = []
                modo = "w"
            
            if hosts:
                print(f"Arquivo hosts já existe. O que deseja fazer?\n")
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
            
            CriarArquivoHosts(caminho, modo, dominios, subdominios)

        else:
            for setor, arquivo in caminho.items():
                print(f"Alterando o arquivo hosts do setor: {setor}.")
                try:
                    with open(arquivo, "r") as file:
                        hosts = file.readlines()
                        file.close()
            
                except FileNotFoundError:
                    hosts = []
                    modo = "w"
                
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
                
                CriarArquivoHosts(arquivo, modo, dominios, subdominios)

    elif opcao == 0:
        print("Encerrando...")
        exit()

    else:
        print("Opção inválida! Informe novamente.\n")
