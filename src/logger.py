import logging
import os
from logging.handlers import RotatingFileHandler

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "infrawatch.log")

def configurar_logger():
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger("infrawatch")
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger
    
    formato = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler_arquivo = RotatingFileHandler(
        LOG_FILE, maxBytes=1_000_000, backupCount=3, enconding="utf-8"
    )
    handler_arquivo.setLevel(logging.DEBUG)
    handler_arquivo.setFormatter(formato)

    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.INFO)
    handler_console.setFormatter(formato)

    logger.addHandler(handler_arquivo)
    logger.addHandler(handler_console)

    return logger

def obter_logger(nome_modulo)
    return logging.getLogger(f"infrawatch.{nome_modulo}")