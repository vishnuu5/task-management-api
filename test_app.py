import unittest
from app import app  # Import the Flask app
import json

class TaskManagementAPITestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_create_task(self):
        # Test the POST /tasks endpoint
        response = self.app.post(
            "/tasks",
            data=json.dumps({
                "title": "Test Task",
                "description": "This is a test task.",
                "due_date": "2024-12-31"
            }),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("id", data)
        self.assertEqual(data["title"], "Test Task")
        self.assertEqual(data["status"], "pending")

    def test_get_tasks(self):
        # Test the GET /tasks endpoint
        response = self.app.get("/tasks")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_update_task(self):
        # Create a task first
        create_response = self.app.post(
            "/tasks",
            data=json.dumps({
                "title": "Test Task",
                "description": "This is a test task.",
                "due_date": "2024-12-31"
            }),
            content_type="application/json"
        )
        task_id = json.loads(create_response.data)["id"]

        # Test the PUT /tasks/{id} endpoint
        update_response = self.app.put(
            f"/tasks/{task_id}",
            data=json.dumps({
                "title": "Updated Task",
                "description": "Updated description.",
                "due_date": "2024-12-25",
                "status": "in_progress"
            }),
            content_type="application/json"
        )
        self.assertEqual(update_response.status_code, 200)
        updated_data = json.loads(update_response.data)
        self.assertEqual(updated_data["title"], "Updated Task")
        self.assertEqual(updated_data["status"], "in_progress")

    def test_delete_task(self):
        # Create a task first
        create_response = self.app.post(
            "/tasks",
            data=json.dumps({
                "title": "Task to Delete",
                "description": "This task will be deleted.",
                "due_date": "2024-12-20"
            }),
            content_type="application/json"
        )
        task_id = json.loads(create_response.data)["id"]

        # Test the DELETE /tasks/{id} endpoint
        delete_response = self.app.delete(f"/tasks/{task_id}")
        self.assertEqual(delete_response.status_code, 204)

        # Verify the task is deleted
        get_response = self.app.get(f"/tasks/{task_id}")
        self.assertEqual(get_response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
