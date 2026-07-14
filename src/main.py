from monitoramento import testar_ping

def solicitar_host():
    return input("Digite o host: ")

def mostrar_menu():
    print("\n===== InfraWatch =====\n")
    print("1. Digitar Host")
    print("2. Testar Ping")
    print("3. Testar SNMP")
    print("4. Verificar memória")
    print("0. Sair")

    return input("Selecione uma opção: ")

def main():
    host = None

    while True:
        opcao = mostrar_menu()

        if opcao == "0":
            print("Saindo...")
            break

        elif opcao == "1":
            host = solicitar_host()
            print(f"Host definido: {host}")

        elif opcao == "2":
            if not host:
                print("Nenhum host foi informado.")
                print("Escolha a opção 1 primeiro.\n")
                continue

            if verificar_ping(host):
                print(f"{host} está Online.\n")
            else:
                print(f"{host} está Offline.\n")

        elif opcao == "3":
            print("SNMP ainda não implementado.\n")

        elif opcao == "4":
            print("Verificação de memória ainda não implementada.\n")

        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    main()