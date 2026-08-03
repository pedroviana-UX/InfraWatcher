try:
    from src.monitoramento import verificar_ping, diagnostico_completo
except ImportError:
    from monitoramento import verificar_ping, diagnostico_completo

try:
    from src.logger import configurar_logger, obter_logger
except ImportError:
    from logger import configurar_logger, obter_logger

logger = obter_logger(__name__)

def solicitar_host():
    return input("Digite o host: ")

def exibir_diagnostico(resultados):
    print("\n===== Diagnóstico Completo =====")
    for teste, status in resultados.items():
        if status is True:
            print(f"{teste.upper()}: OK")
        elif status is False:
            print(f"{teste.upper()}: FALHOU")
        else:
            print(f"{teste.upper()}: não implementado")

def mostrar_menu():
    print("\n===== InfraWatch =====\n")
    print("1. Digitar Host")
    print("2. Testar Ping")
    print("3. Testar SNMP")
    print("4. Verificar memória")
    print("5. Rodar diagnóstico completo")
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

        elif opcao == "5":
            if not host:
                logger.warning("Tentativa de diagnóstico completo sem host definido.")
                print("Nenhum host foi informado.")
                print("Escolha a opção 1 primeiro.\n")
                continue
            resultados = diagnostico_completo(host)
            exibir_diagnostico(resultados)

        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    main()