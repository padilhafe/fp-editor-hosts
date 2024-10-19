def MenuArquivos(arquivos):
    while True:
        print("Selecione uma das opções:")
        for i, chave in enumerate(arquivos.keys(), 1):
            print(f"{i}. {chave}")

        print("0. Voltar")

        try:
            opcao = int(input("> "))
            if 1 <= opcao <= len(arquivos):
                chave_selecionada = list(arquivos.keys())[opcao - 1]
                return arquivos[chave_selecionada]
            elif opcao == 0:
                print("Operação cancelada.")
                exit()
            else:
                print("Opção inválida! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
