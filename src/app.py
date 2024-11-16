# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
todos = []

@app.route('/todos', methods=['GET'])
def get_todos():

    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    todo = {
        'id': len(todos) + 1,
        'title': data['title'],
        'description': data.get('description', ''),
        'done': False
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)

    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    todo = next((todo for todo in todos if todo['id'] == todo_id), None)
    
    if todo is None:
        return jsonify({'error': 'Todo not found'}), 404
    todo['title'] = data.get('title', todo['title'])
    todo['description'] = data.get('description', todo['description'])
    todo['done'] = data.get('done', todo['done'])
    return jsonify(todo)

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)