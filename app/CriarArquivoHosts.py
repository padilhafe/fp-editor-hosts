def CriarArquivoHosts(arquivo, dominios, subdominios):
    with open(arquivo, "w") as file:
        for dominio in dominios:
            for subdominio in subdominios['subdominios']:
                file.write(f"127.0.0.0.1 {subdominio}.{dominio}\n")
