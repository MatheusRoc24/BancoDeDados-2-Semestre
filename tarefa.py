from conexao import get_conexao
from psycopg2.extras import RealDictCursor
from flask import jsonify


def buscar_tarefas():
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