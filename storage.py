from datetime import datetime
from uuid import uuid4

class TaskStorage:
    def __init__(self):
        # In-memory task storage
        self.tasks = {}

    def get_all_tasks(self):
        """Retrieve all tasks."""
        return list(self.tasks.values())

    def get_task(self, task_id):
        """Retrieve a task by ID."""
        return self.tasks.get(task_id)

    def create_task(self, title, description, due_date):
        """Create a new task."""
        task_id = str(uuid4())
        now = datetime.utcnow().isoformat()
        task = {
            "id": task_id,
            "title": title,
            "description": description,
            "due_date": due_date,
            "status": "pending",
            "created_at": now,
            "updated_at": now,
        }
        self.tasks[task_id] = task
        return task

    def update_task(self, task_id, title, description, due_date, status=None):
        """Update an existing task."""
        task = self.tasks.get(task_id)
        if not task:
            return None
        task.update(
            {
                "title": title,
                "description": description,
                "due_date": due_date,
                "status": status or task["status"],
                "updated_at": datetime.utcnow().isoformat(),
            }
        )
        return task

    def delete_task(self, task_id):
        """Delete a task."""
        return self.tasks.pop(task_id, None)

    def mark_task_complete(self, task_id):
        """Mark a task as complete."""
        task = self.tasks.get(task_id)
        if not task:
            return None
        task["status"] = "completed"
        task["updated_at"] = datetime.utcnow().isoformat()
        return task
