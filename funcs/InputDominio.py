def InputDominio():
    dominios = []
    while True:
        dominio = input("Qual domínio deseja adicionar? (ou digite 'sair' para finalizar): ")
        if dominio.lower() == 'sair':
            break
        dominios.append(dominio)
    
    return dominios