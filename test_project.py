import os
import pytest
from project import load_data, add_note, delete_note, calculate_stats, search_notes


def test_add_and_load_note(tmp_path):
    test_file = tmp_path / "test_notes.json"

    # Test adding a note
    note = add_note("Python", "Variables and Data Types", filepath=str(test_file))
    assert note["subject"] == "Python"
    assert note["content"] == "Variables and Data Types"

    # Test loading notes
    notes = load_data(filepath=str(test_file))
    assert len(notes) == 1
    assert notes[0]["subject"] == "Python"


def test_delete_note(tmp_path):
    test_file = tmp_path / "test_notes.json"

    add_note("Math", "Algebra formulas", filepath=str(test_file))
    add_note("CS50", "Functions", filepath=str(test_file))

    # Delete the first note
    delete_note(1, filepath=str(test_file))

    notes = load_data(filepath=str(test_file))
    assert len(notes) == 1
    assert notes[0]["subject"] == "CS50"


def test_calculate_stats(tmp_path):
    test_file = tmp_path / "test_notes.json"

    add_note("Python", "Lists", filepath=str(test_file))
    add_note("Python", "Dictionaries", filepath=str(test_file))
    add_note("Web Dev", "HTML Basics", filepath=str(test_file))

    stats = calculate_stats(filepath=str(test_file))
    assert stats["total_notes"] == 3
    assert stats["total_subjects"] == 2
    assert "Python" in stats["subjects_list"]
    assert "Web Dev" in stats["subjects_list"]

def test_search_notes(tmp_path):
    f = str(tmp_path / "n.json")
    add_note("Python", "Lists and tuples", filepath=f)
    add_note("Math", "Algebra", filepath=f)
    assert len(search_notes("python", filepath=f)) == 1
    assert len(search_notes("", filepath=f)) == 2
    assert search_notes("zzz", filepath=f) == []


def test_unique_ids_after_delete(tmp_path):
    f = str(tmp_path / "n.json")
    add_note("A", "one", filepath=f)
    add_note("B", "two", filepath=f)
    delete_note(1, filepath=f)
    new = add_note("C", "three", filepath=f)
    assert new["id"] == 3
