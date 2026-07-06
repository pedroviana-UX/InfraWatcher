def solicitar_host():
    host = input("Digite o host:")
    return host
def mostrar_menu():
    print("\n===== InfraWatch =====\n")
    print("1. Digitar Host")
    print("2. Testar Ping")
    print("3. Testar SNMP")
    print("4. Verificar memória")
    print("0. Sair")
    opcao = input("Selecione uma opcao")
    return opcao
def testar_ping(host):
    if host:
        print(f"Testando ping para {host}...")
    else:
        print("Nenhum host definido ainda!")    

host = None

while True:
    opcao = mostrar_menu()
    if opcao == "0":
        print("Saindo...")
        break

    elif opcao == "1":
        host = solicitar_host()

    elif opcao == "2":
        testar_ping(host)

    elif opcao == "3":
        print("SNMP ainda não implementado")

    elif opcao == "4":
        print("Verificação de memória ainda não implementada")

    else:
        print("Opção inválida!")