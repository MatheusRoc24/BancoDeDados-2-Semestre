# Importação das bibliotecas
from flask import Flask, request
from tarefa import buscar_tarefas, buscar_tarefa

# Cria o objeto do flask
app = Flask(__name__)

# Criando nossa primeira rota /api
@app.route('/api')
def index():
    return 'Api rodando'

# Criando a rota que retorna as tarefas
@app.route('/api/tarefas')
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas

@app.route('/api/tarefas/<int:tarefa_id>')
def get_tarefa(tarefa_id):
    tarefa = buscar_tarefa(tarefa_id)
    return tarefa


@app.route('/api/tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.json
    from tarefa import inserir_tarefa
    resultado = inserir_tarefa(dados.get('nome'), dados.get('descricao'))
    return resultado


@app.route('/api/tarefas/<int:tarefa_id>', methods=['PUT'])
def atualizar_tarefa(tarefa_id):
    dados = request.json
    from tarefa import atualizar_tarefa as update_tarefa
    resultado = update_tarefa(tarefa_id, dados.get('nome'), dados.get('descricao'))
    return resultado


@app.route('/api/tarefas/<int:tarefa_id>', methods=['DELETE'])
def deletar_tarefa(tarefa_id):
    from tarefa import deletar_tarefa as delete_tarefa
    resultado = delete_tarefa(tarefa_id)
    return resultado
# E liga o servidor executando o Flask 😊
if __name__ == "__main__":
    app.run(debug=True)

  

