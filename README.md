# Task Management API

## Overview
This project is a RESTful API for managing tasks. It allows users to perform CRUD operations on tasks and mark tasks as complete.

## Features
- Create, Read, Update, and Delete tasks
- Mark tasks as complete
- Input validation and error handling
- Unit tests for critical API endpoints

## Technologies
- Python 3.7+
- Flask
- Unittest (for testing)

## Prerequisites
- Python 3.7 or later
- pip (Python package manager)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/vishnuu5/task-management-api.git
   cd task-management-api
   ```

2. Install dependencies:
   ``` bash 
   pip install -r requirements.txt
   ```   

3. Run the Flask app:
   ``` bash 
   python app.py
   ```

4. Access the API at:

Base URL: http://127.0.0.1:5000
Example: GET /tasks   

5. Running Tests:
    ``` bash
    python -m unittest test_app.py
    ```



# API Endpoints:

## Method	     Endpoint	              Description
   GET	         /tasks	                  Retrieve all tasks
   GET	         /tasks/<id>	          Retrieve a specific task
   POST	         /tasks	                  Create a new task
   PUT	         /tasks/<id>	          Update a task
   DELETE	     /tasks/<id>	          Delete a task
   PATCH	     /tasks/<id>/complete	  Mark a task as complete
