# StudyMate

#### Video Demo: https://youtu.be/7I6E95PHuEM

#### Description:

## 1. Overview

StudyMate is a web-based personal study assistant developed using Python and Flask as my CS50P final project. It is designed to help students organise their study notes and keep track of their learning materials in one convenient place.

Students often create notes across different subjects, making it difficult to locate specific information when they need to revise. StudyMate addresses this problem by providing a simple interface for adding, viewing, searching, and deleting notes. Each note contains a subject and its content, helping students keep their study materials organised.

The application includes a dashboard that provides an overview of saved study materials through statistics such as the total number of notes, the number of subjects covered, and recently added notes. This allows users to understand their collection of study materials without browsing through every note.

I chose this project because it combines Python programming concepts with practical web development. It gave me an opportunity to practise functions, data structures, file handling, exception handling, automated testing, and Flask application development while building something useful for students.

## 2. How to Run the Project

Python 3 must be installed before running StudyMate.

Navigate to the project directory and install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python project.py
```

Open the following address in your browser:

http://127.0.0.1:5000

Keep the terminal running while using the application. Stop the development server by pressing `Ctrl+C`.

## 3. Project Files and Implementation

### `project.py`

This is the main application file. It contains the Flask application, the data-management functions, and the routes that connect the backend to the website.

- **`ensure_data_directory()`** ensures that the directory used for storing application data exists. If the directory is missing, it creates it.
- **`load_data(filepath)`** reads saved data from a JSON file and converts it into Python data structures. It handles missing files and invalid JSON according to the application's error-handling logic.
- **`save_data(data, filepath)`** writes updated data to a JSON file, allowing notes to persist after the application is restarted.
- **`add_note(...)`** adds a new note containing the relevant information, such as its identifier, subject, and content.
- **`delete_note(...)`** removes a selected note using its identifier.
- **`search_notes(...)`** searches saved notes using a text query, such as a subject or words contained in the note.
- **`calculate_stats(...)`** calculates the information displayed on the dashboard, such as the number of notes and subjects.
- **`main()`** ensures that the data directory exists and starts the Flask development server.

The Flask routes handle browser requests, retrieve submitted form data, call the appropriate logic functions, and render HTML templates with the required information. Keeping the data-management logic separate from the Flask routes makes the application easier to maintain and test.

Where appropriate, the data-management functions accept a file path as an argument. This allows them to work with the application's normal data file or with a temporary file during testing. Consequently, tests can verify the behaviour of individual functions without modifying the user's actual notes.

### `test_project.py`

This file contains automated tests written using pytest. The tests verify important application functions, including adding notes, searching notes, deleting notes, and calculating dashboard statistics.

The `tmp_path` fixture provided by pytest creates temporary file locations for test data. This allows each test to work with its own JSON file instead of modifying the application's actual `data/notes.json` file.

Using temporary files makes tests more isolated, repeatable, and reliable. It also helps identify errors in the application's logic before the project is submitted.

Run the tests using:

```bash
pytest -q
```

### `templates/`

This directory contains the HTML templates used to display the StudyMate website.

- **`index.html`** serves as the main landing page and provides navigation to the application's features.
- **`dashboard.html`** displays an overview of study materials, including relevant note statistics and recently added notes.
- **`notes.html`** provides the interface for adding, viewing, searching, and deleting study notes.

Separating the pages into individual templates keeps the website organised and makes it easier to update each page independently. Flask passes the relevant data to the templates so that displayed information can reflect the saved notes.

### `static/style.css`

This file contains the CSS used to style the application. It controls the layout, colours, typography, navigation, forms, and note cards. Keeping the styling separate from the HTML makes the website easier to maintain and customise.

### `data/notes.json`

This file stores the application's notes in JSON format. A note can contain an identifier, a subject, and its content.

JSON is human-readable and can be loaded into Python dictionaries and lists for processing. The application can save updated notes to this file so that the data remains available after restarting the server. The data directory and file can be initialised when required by the application.

## 4. Design Decisions

I chose Flask because it provides a simple way to build a web application using Python without requiring a large web framework. It connects the Python backend to HTML templates and handles requests submitted through the browser.

I chose JSON for data storage because the project is a small, local application with straightforward data requirements. JSON is easy to inspect, requires no separate database server, and integrates naturally with Python. A database could be considered in the future if the application needs more complex queries, larger amounts of data, or support for multiple users.

Each note has an identifier so that it can be selected for deletion independently of its position in the list. When generating a new identifier, using the highest existing ID plus one avoids reusing an identifier simply because a note with a larger ID was deleted.

I deliberately limited the initial scope to the dashboard and notes management instead of implementing quizzes, a revision planner, and settings. Focusing on these two core features allowed me to concentrate on implementing and testing the essential functionality.

Future improvements could include editing existing notes, filtering notes by subject, adding study goals, expanding dashboard statistics, and introducing an AI-powered study assistant.

## 5. Conclusion

StudyMate demonstrates how Python, Flask, HTML, CSS, JSON, and pytest can be combined to build a practical web application. Through this project, I gained experience in writing reusable functions, managing persistent data, handling web requests, and testing application logic independently.

The project provides a foundation for future enhancements while keeping the initial implementation focused on helping students organise and access their study notes efficiently.
