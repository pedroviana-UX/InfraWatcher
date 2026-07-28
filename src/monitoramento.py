import platform
import subprocess

try: 
    from src.logger import obter_logger
except ImportError:
    from logger import obter_logger

logger = obter_logger(__name__)


def verificar_ping(host):
    if not host:
        logger.warning("Tentativa de ping sem host informado.")
        return False

    parametro = "-n" if platform.system() == "Windows" else "-c"

    logger.debug("Iniciando ping para host=%s", host)

    try:
        resultado = subprocess.run(
            ["ping", parametro, "1", host],
            capture_output=True,
            text=True,
        )

        if resultado.returncode == 0:
            logger.info("Host %s está Online.", host)
            return True
        
        logger.info("Host %s está Offline.", host)
        return False

    except FileNotFoundError:
        logger.error("Comando 'ping' não encontrado no sistema.")
        print("Comando 'ping' não encontrado. ")
        return False