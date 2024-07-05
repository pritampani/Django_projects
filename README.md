# Toto List

Toto List is a simple Django-based to-do list application that allows users to create and delete to-do items. The application features a single HTML page that interacts with the Django backend.

## Features

- **Create To-Do Item**: Add a new item to your to-do list.
- **Delete To-Do Item**: Remove an item from your to-do list.

## Requirements

- Python 3.x
- Django 3.x or 4.x

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/toto-list.git
    cd toto-list
    ```

2. **Create a virtual environment**:

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

5. **Run migrations**:

    ```sh
    python manage.py migrate
    ```

6. **Start the development server**:

    ```sh
    python manage.py runserver
    ```

7. **Access the application**:

    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Creating a To-Do Item

1. Navigate to the main page of the application.
2. Enter the title of the to-do item in the input field.
3. Click the "Add" button to create the to-do item.

### Deleting a To-Do Item

1. Navigate to the main page of the application.
2. Click the "Delete" button next to the to-do item you want to remove.

## Project Structure

- **toto_list/**: Main Django project folder.
- **toto_app/**: Django app folder containing models, views, and templates.
- **templates/**: Folder containing the HTML template.
- **static/**: Folder containing static files (CSS, JavaScript).

## File Overview

- **toto_list/settings.py**: Django project settings.
- **toto_list/urls.py**: URL configurations for the project.
- **toto_app/models.py**: Defines the ToDo model.
- **toto_app/views.py**: Handles request and response logic for creating and deleting to-do items.
- **toto_app/urls.py**: URL configurations for the app.
- **templates/todo_list.html**: The single HTML page used in the project.

## Example Code

### `models.py`

```python
from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
