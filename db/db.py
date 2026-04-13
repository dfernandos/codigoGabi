import sqlite3

DATABASE = "focusfluir.db"


def conexao():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def iniciar_nova_sessao(tempo_estudo: int, tempo_pausa: int, playlist_id: int) -> int:
    conn = conexao()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sessoes (duracao_programada_estudo, duracao_programada_pausa, playlist_id) VALUES (?, ?, ?)",
        (tempo_estudo, tempo_pausa, playlist_id),
    )
    conn.commit()
    sessao_id = cursor.lastrowid
    conn.close()
    return sessao_id
