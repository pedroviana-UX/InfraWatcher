from unittest.mock import patch, MagicMock

from src.monitoramento import verificar_ping, host_e_valido, diagnostico_completo


def test_host_vazio():
    assert verificar_ping("") is False


def test_host_vazio_gera_aviso_no_log(caplog):
    with caplog.at_level("WARNING"):
        verificar_ping("")

    assert "Tentativa de ping sem host informado." in caplog.text


def test_host_valido_ip():
    assert host_e_valido("8.8.8.8") is True


def test_host_valido_hostname():
    assert host_e_valido("meuhost.local") is True


def test_host_invalido_com_injecao():
    assert host_e_valido("8.8.8.8; rm -rf /") is False


def test_host_invalido_vazio():
    assert host_e_valido("") is False


def test_host_invalido_comeca_ponto():
    assert host_e_valido(".host.com") is False


def test_verificar_ping_host_online():
    with patch("src.monitoramento.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0)

        resultado = verificar_ping("qualquer.host")

        assert resultado is True


def test_verificar_ping_host_offline():
    with patch("src.monitoramento.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=1)

        resultado = verificar_ping("qualquer.host")

        assert resultado is False


def test_diagnostico_completo_ping_ok():
    with patch("src.monitoramento.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=0)

        resultados = diagnostico_completo("8.8.8.8")

        assert resultados["ping"] is True
        assert resultados["snmp"] is None
        assert resultados["memoria"] is None


def test_diagnostico_completo_ping_falha():
    with patch("src.monitoramento.subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(returncode=1)

        resultados = diagnostico_completo("8.8.8.8")

        assert resultados["ping"] is False
