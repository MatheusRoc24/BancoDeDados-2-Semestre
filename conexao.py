<<<<<<< HEAD
import psycopg2


def get_conexao():
    conn = psycopg2.connect(
        dbname="todolist",  
        user = 'postgres',
        password = 'admin',
        host = '127.0.0.1',
        port = '1024',
    )
=======
import psycopg2


def get_conexao():
    conn = psycopg2.connect(
        dbname="todolist",  
        user = 'postgres',
        password = 'admin',
        host = '127.0.0.1',
        port = '1024',
    )
>>>>>>> b55925e (bd)
    return conn