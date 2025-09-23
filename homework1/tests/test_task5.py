import sys
import os
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
task_dir = os.path.join(current_dir, '../src')
sys.path.insert(0, task_dir)

import task5

def test_books_list_exists_and_length():
    assert isinstance(task5.books, list)
    assert len(task5.books) >= 3

def test_first_three_books_slice():
    expected = task5.books[:3]
    assert task5.first_three_books == expected

def test_book_items_structure():
    # each book should be a tuple (title, author)
    for book in task5.books:
        assert isinstance(book, tuple)
        assert len(book) == 2
        title, author = book
        assert isinstance(title, str)
        assert isinstance(author, str)

def test_students_dict_structure():
    assert isinstance(task5.students, dict)
    assert len(task5.students) >= 3

def test_student_id_format():
    for name, sid in task5.students.items():
        assert isinstance(name, str)
        assert isinstance(sid, str)
        # id starts with 'S' and has numbers after
        assert sid.startswith("S")
        assert sid[1:].isdigit()
