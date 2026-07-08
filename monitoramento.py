import subprocess

def testar_ping(host, parametro):

    if not host:
        return False

    resultado = subprocess.run(["ping", parametro, "1", host])

    print(resultado)

    return resultado.returncode == 0