from flask import Flask, jsonify, request

app = Flask(__name__)

# Simple in-memory list of dictionaries
todos = [
    {"id": 1, "title": "Finish homework", "done": False},
    {"id": 2, "title": "Buy groceries", "done": False}
]

# 1. GET /todos - Get all todos
@app.route('/todos', methods=['GET'])
def get_all():
    return jsonify(todos)

# 2. GET /todos/<id> - Get one todo
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_one(todo_id):
    # Find the first item where the id matches
    todo = next((t for t in todos if t['id'] == todo_id), None)
    return jsonify(todo)

# 3. POST /todos - Create a new todo
@app.route('/todos', methods=['POST'])
def create():
    new_todo = {
        "id": len(todos) + 1,
        "title": request.json['title'],
        "done": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

# 4. PUT /todos/<id> - Update a todo
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    # Update fields from the request body
    todo['title'] = request.json.get('title', todo['title'])
    todo['done'] = request.json.get('done', todo['done'])
    return jsonify(todo)

# 5. DELETE /todos/<id> - Delete a todo
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete(todo_id):
    global todos
    # Keep every todo EXCEPT the one with the matching id
    todos = [t for t in todos if t['id'] != todo_id]
    return jsonify({"message": "Deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)