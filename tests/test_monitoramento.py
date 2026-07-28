from src.monitoramento import verificar_ping

def test_host_vazio():
    assert verificar_ping("") is False


def test_host_vazio_gera_aviso_no_log(caplog):
    with caplog.at_level("WARNING"):
        verificar_ping("")

    assert "Tentativa de ping sem host informado." in caplog.text