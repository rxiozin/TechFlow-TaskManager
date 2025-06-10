from flask import Flask, jsonify, request, abort, render_template

app = Flask(__name__)

# Inicializo a lista que vai guardar as tarefas
tasks = []
# Variável para controlar o próximo ID que vou atribuir a uma nova tarefa
next_id = 1

@app.route('/')
def serve_index():
    # Retorno a página HTML principal (index.html)
    return render_template('index.html')

# Rota para listar todas as tarefas, com filtro opcional por status de conclusão
@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Pego o parâmetro 'completed' da query string (ex: ?completed=true)
    completed = request.args.get('completed')
    if completed is not None:
        # Se o parâmetro for 'true', filtro só as tarefas concluídas
        if completed.lower() == 'true':
            filtered = [t for t in tasks if t['completed'] is True]
        # Se for 'false', filtro as tarefas não concluídas
        elif completed.lower() == 'false':
            filtered = [t for t in tasks if t['completed'] is False]
        else:
            # Se o parâmetro não for válido, retorno erro 400 (Bad Request)
            abort(400, 'Parâmetro completed inválido')
        # Retorno a lista filtrada em JSON
        return jsonify(filtered)
    # Se não tiver filtro, retorno todas as tarefas
    return jsonify(tasks)

# Rota para criar uma nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    # Verifico se recebi JSON e se tem o campo 'title'
    if not request.json or 'title' not in request.json:
        abort(400, 'Título da tarefa é obrigatório')
    # Crio um dicionário com os dados da nova tarefa
    task = {
        'id': next_id,                  # ID único que vai aumentando
        'title': request.json['title'],# Título da tarefa vindo da requisição
        'completed': False             # Sempre começo como não concluída
    }
    # Adiciono a tarefa na lista
    tasks.append(task)
    # Incremento o ID para a próxima tarefa
    next_id += 1
    # Retorno a tarefa criada e o status HTTP 201 (Created)
    return jsonify(task), 201

# Rota para atualizar uma tarefa específica pelo ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Procuro a tarefa pelo ID na lista
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        # Se não encontrar, retorno erro 404 (Not Found)
        abort(404, 'Tarefa não encontrada')
    if not request.json:
        # Se não veio JSON na requisição, erro 400
        abort(400, 'JSON obrigatório')

    # Pego os campos title e completed do JSON, se não vier uso os atuais
    title = request.json.get('title', task['title'])
    completed = request.json.get('completed', task['completed'])

    # Verifico se os tipos estão corretos (title deve ser string, completed bool)
    if not isinstance(title, str) or not isinstance(completed, bool):
        abort(400, 'Campos inválidos')

    # Atualizo a tarefa com os novos valores
    task['title'] = title
    task['completed'] = completed
    # Retorno a tarefa atualizada
    return jsonify(task)

# Rota para deletar uma tarefa pelo ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    # Procuro a tarefa na lista
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        # Se não encontrar, retorno 404
        abort(404, 'Tarefa não encontrada')
    # Removo a tarefa da lista filtrando ela para fora
    tasks = [t for t in tasks if t['id'] != task_id]
    # Retorno status 204 (No Content), pois delete não retorna corpo
    return '', 204

if __name__ == '__main__':
    # Executo o servidor Flask em modo debug (recarrega automático e mostra erros)
    app.run(debug=True)
