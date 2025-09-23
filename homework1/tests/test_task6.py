import sys
import os
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
task_dir = os.path.join(current_dir, '../src')
sys.path.insert(0, task_dir)

from task6 import count_words_in_file

def test_count_words_simple_file(tmp_path):
    # fake temporary file for testing
    content = "this is a test file.\nit has words."
    file_path = tmp_path / "test_file.txt"
    file_path.write_text(content)

    # Counts words
    count = count_words_in_file(file_path)

    # 8 words
    assert count == 8

def test_count_words_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"
    file_path.write_text("")  # empty file

    # 0 words
    count = count_words_in_file(file_path)
    assert count == 0

def test_count_words_task6_read_me():
    # This was only found if the file was in the directory that you run pytest fromm, which is dumb, so i have 3 copies of this just in case.
    # I might lose points for that but waah waaaahhhhhh i dont care i want to die
    count = count_words_in_file("task6_read_me.txt")
    assert count == 127
