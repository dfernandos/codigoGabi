import json
from unittest.mock import patch

from service.service import iniciar_foco_salvar


@patch("service.service.db")
@patch("service.service.iniciar_foco_validar")
def test_iniciar_foco_salvar_chama_db_quando_valido(mock_validar, mock_db):

    # Dado que o validar retorna True
    mock_validar.return_value = True
    # Dado que o db.iniciar_nova_sessao retorna {"id": 1}
    mock_db.iniciar_nova_sessao.return_value = {"id": 1}
    # Dado que os objetivos são ["estudar"]
    objetivos = '["estudar"]'
    # Quando iniciar_foco_salvar é chamado com 25, 5, 42 e ["estudar"]
    result = iniciar_foco_salvar(25, 5, 42, objetivos)
    # Então o validar deve ser chamado com 25, 5 e ["estudar"]
    mock_validar.assert_called_once_with(25, 5, objetivos)
    # Então o db.iniciar_nova_sessao deve ser chamado com 25 * 60, 5 * 60 e 42
    mock_db.iniciar_nova_sessao.assert_called_once_with(25 * 60, 5 * 60, 42)
    # Então o resultado deve ser {"id": 1}
    assert result == {"id": 1}

@patch("service.service.iniciar_foco_validar")
def test_iniciar_foco_salvar_retorna_erro_sem_chamar_db(mock_validar):
    mock_validar.return_value = ("Tempo de estudo inválido", 400)
    result = iniciar_foco_salvar(0, 5, None, "[]")
    assert result == ("Tempo de estudo inválido", 400)
