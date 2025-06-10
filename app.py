from flask import Flask, jsonify, request, abort, render_template

app = Flask(__name__,)

tasks = []
next_id = 1

@app.route('/')
def serve_index():
    return render_template('index.html')

# Listar tarefas, opcional filtro por status (?completed=true/false)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    completed = request.args.get('completed')
    if completed is not None:
        if completed.lower() == 'true':
            filtered = [t for t in tasks if t['completed'] is True]
        elif completed.lower() == 'false':
            filtered = [t for t in tasks if t['completed'] is False]
        else:
            abort(400, 'Parâmetro completed inválido')
        return jsonify(filtered)
    return jsonify(tasks)

# Criar nova tarefa
@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    if not request.json or 'title' not in request.json:
        abort(400, 'Título da tarefa é obrigatório')
    task = {
        'id': next_id,
        'title': request.json['title'],
        'completed': False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

# Atualizar tarefa (title e completed)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        abort(404, 'Tarefa não encontrada')
    if not request.json:
        abort(400, 'JSON obrigatório')

    title = request.json.get('title', task['title'])
    completed = request.json.get('completed', task['completed'])

    if not isinstance(title, str) or not isinstance(completed, bool):
        abort(400, 'Campos inválidos')

    task['title'] = title
    task['completed'] = completed
    return jsonify(task)

# Deletar tarefa
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        abort(404, 'Tarefa não encontrada')
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
