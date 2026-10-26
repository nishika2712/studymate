from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

DATA_DIR = "data"
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")


# --- Core Logic Functions ---

def ensure_data_directory():
    """Ensure the data folder exists."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def load_data(filepath=NOTES_FILE):
    """Load JSON data safely."""
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(data, filepath=NOTES_FILE):
    """Save JSON data safely."""
    ensure_data_directory()
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


def add_note(subject, content, filepath=NOTES_FILE):
    notes = load_data(filepath)
    new_id = max((n["id"] for n in notes), default=0) + 1
    new_note = {"id": new_id, "subject": subject, "content": content}
    notes.append(new_note)
    save_data(notes, filepath)
    return new_note


def search_notes(query, filepath=NOTES_FILE):
    """Return notes whose subject or content contains the query."""
    notes = load_data(filepath)
    query = query.strip().lower()
    if not query:
        return notes
    return [
        n for n in notes
        if query in n["subject"].lower() or query in n["content"].lower()
    ]

def delete_note(note_id, filepath=NOTES_FILE):
    """Delete a note by ID."""
    notes = load_data(filepath)
    notes = [n for n in notes if n.get("id") != note_id]
    save_data(notes, filepath)


def calculate_stats(filepath=NOTES_FILE):
    """Calculate dashboard statistics."""
    notes = load_data(filepath)
    subjects = set(n["subject"] for n in notes if "subject" in n)
    return {
        "total_notes": len(notes),
        "total_subjects": len(subjects),
        "subjects_list": sorted(list(subjects))
    }


# --- Web Routes ---

@app.route("/")
def index():
    """Main Menu Page"""
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    """Dashboard Page"""
    stats = calculate_stats()
    return render_template("dashboard.html", stats=stats)


@app.route("/notes", methods=["GET", "POST"])
def manage_notes():
    """Manage Notes Page"""
    if request.method == "POST":
        subject = request.form.get("subject", "").strip()
        content = request.form.get("content", "").strip()
        if subject and content:
            add_note(subject, content)
        return redirect(url_for("manage_notes"))

    query = request.args.get("q", "")
    notes = search_notes(query)
    return render_template("notes.html", notes=notes, query=query)


@app.route("/delete_note/<int:note_id>", methods=["POST"])
def handle_delete_note(note_id):
    delete_note(note_id)
    return redirect(url_for("manage_notes"))


def main():
    ensure_data_directory()
    print("Starting StudyMate Web App on http://127.0.0.1:5000")
    app.app_context()
    app.run(debug=True)


if __name__ == "__main__":
    main()
