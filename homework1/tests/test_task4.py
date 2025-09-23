import sys
import os
import pytest

current_dir = os.path.dirname(os.path.abspath(__file__))
task_dir = os.path.join(current_dir, '../src')
sys.path.insert(0, task_dir)

from task4 import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 20) == 80
    assert calculate_discount(50, 50) == 25
    assert calculate_discount(100, 12.5) == 87.5
    assert calculate_discount(200.5, 10) == pytest.approx(180.45)