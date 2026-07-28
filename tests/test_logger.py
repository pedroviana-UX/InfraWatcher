from src.logger import configurar_logger

def test_configurar_logger_nao_duplica_handlers():
    logger1 = configurar_logger()
    quantidade_inicial = len(logger1.handlers)

    logger2 = configurar_logger()
    quantidade_depois = len(logger1.handlers)

    assert quantidade_depois == quantidade_inicial