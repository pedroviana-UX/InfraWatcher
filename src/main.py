from monitoramento import verificar_ping

try:
    from src.logger import configurar_logger, obter_logger
except ImportError:
    from logger import configurar_logger, obter_logger

logger = obter_logger(__name__)

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
    configurar_logger()
    logger.info("Aplicação InfraWatch iniciada. ")

    host = None

    while True:
        opcao = mostrar_menu()

        if opcao == "0":
            print("Saindo...")
            logger.info("Aplicação encerrada pelo usuário.")
            break

        elif opcao == "1":
            host = solicitar_host()
            logger.info("Host definido: %s", host)
            print(f"Host definido: {host}")

        elif opcao == "2":
            if not host:
                logger.warning("Tentativa de testar ping sem host definido.")
                print("Nenhum host foi informado.")
                print("Escolha a opção 1 primeiro.\n")
                continue

            if verificar_ping(host):
                print(f"{host} está Online.\n")
            else:
                print(f"{host} está Offline.\n")

        elif opcao == "3":
            logger.debug("Opção SNMP selecionada. ")
            print("SNMP ainda não implementado.\n")

        elif opcao == "4":
            logger.debug("Opção de verificação de memória selecionada.")
            print("Verificação de memória ainda não implementada.\n")

        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    main()