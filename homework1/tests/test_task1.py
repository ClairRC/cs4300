import sys
import os

# bruh how else am i supposed to do this
current_dir = os.path.dirname(os.path.abspath(__file__))
task_dir = os.path.join(current_dir, '../src')
sys.path.insert(0, task_dir)

from task1 import print_stuff

def test_print_stuff(capsys):
    print_stuff()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"