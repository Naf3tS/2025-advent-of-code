import pytest
from src03b import max_joltage

def test_max_joltage():
    assert max_joltage("123",2) == 23
    assert max_joltage("999",2) == 99

def test_max_joltage_edge_case():
    assert max_joltage("989",2) == 99

def test_bigger_banks():
    assert max_joltage("1234",3) == 234
    assert max_joltage("9876",3) == 987
    assert max_joltage("192837465",4) == 9876