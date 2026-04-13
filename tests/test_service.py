import json
from unittest.mock import patch

from service.service import iniciar_foco_salvar


@patch("service.service.db")
@patch("service.service.iniciar_foco_validar")
def test_iniciar_foco_salvar_chama_db_quando_valido(mock_validar, mock_db):
    mock_validar.return_value = True
    mock_db.iniciar_nova_sessao.return_value = {"id": 1}
    objetivos = json.dumps(["estudar"])
    result = iniciar_foco_salvar(25, 5, 42, objetivos)
    mock_validar.assert_called_once_with(25, 5, objetivos)
    mock_db.iniciar_nova_sessao.assert_called_once_with(25 * 60, 5 * 60, 42)
    assert result == {"id": 1}


@patch("service.service.iniciar_foco_validar")
def test_iniciar_foco_salvar_retorna_erro_sem_chamar_db(mock_validar):
    mock_validar.return_value = ("Tempo de estudo inválido", 400)
    result = iniciar_foco_salvar(0, 5, None, "[]")
    assert result == ("Tempo de estudo inválido", 400)
