import platform
import subprocess
import re

PADRAO_HOST_VALIDO = re.compile(
    r"^[a-zA-Z0-9]([a-zA-Z0-9\-\.]*[a-zA-Z0-9])?$"
)

def host_e_valido(host):
    if not host or len(host) > 253:
        return False
    return bool(PADRAO_HOST_VALIDO.match(host))

try:
    from src.logger import obter_logger
except ImportError:
    from logger import obter_logger

logger = obter_logger(__name__)


def verificar_ping(host):
    if not host:
        logger.warning("Tentativa de ping sem host informado.")
        return False

    if not host_e_valido(host):
        logger.warning("Host inválido informado: %s", host)
        return False
    
    parametro = "-n" if platform.system() == "Windows" else "-c"

    logger.debug("Iniciando ping para host=%s", host)

    try:
        resultado = subprocess.run(
            ["ping", parametro, "1", host],
            capture_output=True,
            text=True,
            timeout=10,
        )
    except subprocess.TimeoutExpired:
        logger.warning("Ping para host %s excedeu o tempo limite.", host)
        return False
    except FileNotFoundError:
        logger.error("Comando 'ping' não encontrado no sistema.")
        print("Comando 'ping' não encontrado.")
        return False

    if resultado.returncode == 0:
        logger.info("Host %s está Online.", host)
        return True

    logger.info("Host %s está Offline.", host)
    return False

def diagnostico_completo(host):
    resultados = {}

    resultados["ping"] = verificar_ping(host)
    resultados["snmp"] = None
    resultados["memoria"] = None

    return resultados