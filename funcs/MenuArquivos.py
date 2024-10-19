def MenuArquivos(arquivos):
    while True:
        print("Selecione uma das opções:")
        for i, chave in enumerate(arquivos.keys(), 1):
            print(f"{i}. {chave}")
        print("99. Todos os arquivos.")
        print("0. Cancelar operação.")

        opcao = int(input("> "))

        if opcao == 0:
            print("Operação cancelada.")
            exit()

        if opcao == 99:
            return arquivos

        try:
            if 1 <= opcao <= len(arquivos):
                chave_selecionada = list(arquivos.keys())[opcao - 1]
                return arquivos[chave_selecionada]
            
            else:
                print("Opção inválida! Tente novamente.")

        except ValueError:
            print("Entrada inválida! Digite um número válido.")
