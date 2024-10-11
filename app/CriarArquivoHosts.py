def CriarArquivoHosts(arquivo, modo, dominios, subdominios):
    with open(arquivo, modo) as file:
        for dominio in dominios:
            for subdominio in subdominios['subdominios']:
                file.write(f"127.0.0.0.1 {subdominio}.{dominio}\n")
