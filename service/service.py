"""
Regras de negócio e orquestração (sem Flask); persistência via db.
"""
import json
import db.db as db
from datetime import datetime, timezone
import service.service as service


def iniciar_foco_validar(tempo_estudo: int, tempo_pausa: int, objetivos: str):
    print(f"Validando tempo de estudo: {tempo_estudo} e tempo de pausa: {tempo_pausa}")
    if tempo_estudo <= 0:
        return "Tempo de estudo inválido", 400
    if tempo_pausa <= 0:
        return "Tempo de pausa inválido", 400

    try:
        lista_objetivos = json.loads(objetivos)
        if not lista_objetivos:
            return "Adicione pelo menos um objetivo", 400
    except json.JSONDecodeError:
        return "Erro nos objetivos", 400

    return True

def iniciar_foco_salvar(
    tempo_estudo_min: int,
    tempo_pausa_min: int,
    playlist_id: int | str | None,
    objetivos: str,
):
    print(f"Salvando sessão com tempo de estudo: {tempo_estudo_min} e tempo de pausa: {tempo_pausa_min} e playlist_id: {playlist_id} e objetivos: {objetivos}")
    
    valido = iniciar_foco_validar(tempo_estudo_min, tempo_pausa_min, objetivos)
    if valido is not True:
        return valido
    ## pid = int(playlist_id) if playlist_id not in (None, "") else None
    return db.iniciar_nova_sessao(
        tempo_estudo_min * 60,
        tempo_pausa_min * 60,
        playlist_id,
    )
