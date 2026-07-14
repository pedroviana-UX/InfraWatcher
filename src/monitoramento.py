import platform
import subprocess


def verificar_ping(host):
    if not host:
        return False

    parametro = "-n" if platform.system() == "Windows" else "-c"

    try:
        resultado = subprocess.run(
            ["ping", parametro, "1", host],
            capture_output=True,
            text=True,
        )

        return resultado.returncode == 0

    except FileNotFoundError:
        print("Comando 'ping' não encontrado.")
        return False