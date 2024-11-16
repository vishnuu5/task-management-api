from flask import Flask, request, jsonify, abort
from storage import TaskStorage


app = Flask(__name__)

# Initialize TaskStorage
task_storage = TaskStorage()

# Helper function to validate task input
def validate_task(data):
    required_fields = ["title", "description", "due_date"]
    for field in required_fields:
        if field not in data:
            abort(400, f"Missing required field: {field}")

# Routes
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(task_storage.get_all_tasks()), 200

@app.route("/tasks/<string:task_id>", methods=["GET"])
def get_task(task_id):
    task = task_storage.get_task(task_id)
    if not task:
        abort(404, "Task not found")
    return jsonify(task), 200

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    validate_task(data)
    task = task_storage.create_task(
        title=data["title"], description=data["description"], due_date=data["due_date"]
    )
    return jsonify(task), 201

@app.route("/tasks/<string:task_id>", methods=["PUT"])
def update_task(task_id):
    task = task_storage.get_task(task_id)
    if not task:
        abort(404, "Task not found")
    data = request.json
    validate_task(data)
    updated_task = task_storage.update_task(
        task_id,
        title=data["title"],
        description=data["description"],
        due_date=data["due_date"],
        status=data.get("status"),
    )
    return jsonify(updated_task), 200

@app.route("/tasks/<string:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if not task_storage.delete_task(task_id):
        abort(404, "Task not found")
    return "", 204

@app.route("/tasks/<string:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    task = task_storage.mark_task_complete(task_id)
    if not task:
        abort(404, "Task not found")
    return jsonify(task), 200

# Error Handlers
@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify({"error": str(e)}), 400

@app.errorhandler(404)
def handle_not_found(e):
    return jsonify({"error": str(e)}), 404

if __name__ == "__main__":
    app.run(debug=True)
