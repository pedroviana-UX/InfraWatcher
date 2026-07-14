from src.monitoramento import verificar_ping

def test_host_vazio():
    assert verificar_ping("") is False