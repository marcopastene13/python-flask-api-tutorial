from flask import Flask,jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json  
    todos.append(request_body)    
    return jsonify(todos) 

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("Esta es la posición a eliminar:", position)
    del todos[position] 
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)