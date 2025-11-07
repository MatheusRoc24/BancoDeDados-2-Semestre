from conexao import get_conexao
<<<<<<< HEAD
from psycopg2.extras import RealDictCursor
=======

from psycopg2.extras import RealDictCursor

>>>>>>> b55925e (bd)
from flask import jsonify


def buscar_tarefas():
<<<<<<< HEAD
    conn = None
    try:
        conn = get_conexao()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        # Chamar execute corretamente (antes estava apenas referenciando a função)
        cursor.execute("SELECT id, nome, descricao FROM tarefas;")
        tarefas = cursor.fetchall()
        cursor.close()
        return jsonify(tarefas)
    except Exception as e:
        # Retorna erro em JSON para facilitar depuração no cliente
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()
=======
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute
    (
        "SELECT id, nome, descricao FROM tarefas;"
    )
    tarefas = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(tarefas)
>>>>>>> b55925e (bd)
