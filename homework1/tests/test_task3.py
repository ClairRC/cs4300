import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
task_dir = os.path.join(current_dir, '../src')
sys.path.insert(0, task_dir)

from task3 import isPositive
from task3 import findFirstNPrimes
from task3 import sumOfFirstNNumbers

def test_isPositive():
    assert isPositive(1293) == 1
    assert isPositive(1.43) == 1
    assert isPositive(0) == 0
    assert isPositive(-1.3) == -1

def test_findFirstNPrimes():
    first_1_primes = [2]
    first_2_primes = [2, 3]
    first_5_primes = [2, 3, 5, 7, 11]
    first_10_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    assert findFirstNPrimes(0) == []
    assert findFirstNPrimes(1) == first_1_primes
    assert findFirstNPrimes(2) == first_2_primes
    assert findFirstNPrimes(5) == first_5_primes
    assert findFirstNPrimes(10) == first_10_primes

def test_sumOfFirstNNumbers():
    assert sumOfFirstNNumbers(0) == 0
    assert sumOfFirstNNumbers(1) == 1
    assert sumOfFirstNNumbers(50) == 1275
    assert sumOfFirstNNumbers(100) == 5050