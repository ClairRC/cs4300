import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_dir = os.path.join(current_dir, '../src')
sys.path.insert(0, task_dir)

from task2 import int_multiplication
from task2 import float_addition
from task2 import print_hello
from task2 import not_gate

def test_int_multiplication():
    assert int_multiplication(1, 3) == 3
    assert int_multiplication(3, 4) == 12
    assert int_multiplication(12, 12) == 144

def test_float_addition():
    assert float_addition(1.3, 2.5) == 3.8
    assert float_addition(3.5, 1.5) == 5.0
    assert float_addition(6.5, 4) == 10.5

def test_print_hello(capsys):
    print_hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello"

def test_not_gate():
    assert not_gate(False) == True
    assert not_gate(True) == False