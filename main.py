
import platform

sistema = platform.system()
if sistema == "Windows":
    parametro = "-n"
else:
    parametro = "-c"

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
    opcao = input("Selecione uma opcao\n")
    return opcao

from monitoramento import testar_ping

host = None

while True:
    opcao = mostrar_menu()
    if opcao == "0":
        print("Saindo...")
        break

    elif opcao == "1":
        host = solicitar_host()

    elif opcao == "2":
        resultado = testar_ping(host)
        if resultado:
            print(f"{host} Online")
        else:
            print(f"{host} Offline")

    elif opcao == "3":
        print("SNMP ainda não implementado")

    elif opcao == "4":
        print("Verificação de memória ainda não implementada")

    else:
        print("Opção inválida!")
