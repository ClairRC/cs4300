import sys
import os
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
task_dir = os.path.join(current_dir, '../src')
sys.path.insert(0, task_dir)

from task7 import get_word_count_from_url

def test_word_count_known_url():
    # Does NOT have very many words
    url = "https://www.example.com/"
    count = get_word_count_from_url(url)

    assert count < 200
    assert count > 0

def test_invalid_url():
    with pytest.raises(Exception):
        get_word_count_from_url("https://definitely_real_as_frick.whocares")
