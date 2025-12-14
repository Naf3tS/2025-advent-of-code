import pytest
from src02b import check_id_range, is_valid_id

IS_INVALID_ID = (0,0,0)

def test_id_range_valid():
    out = check_id_range("123-124")
    assert out==(2,0,0)

def test_id_range_mixed():
    assert check_id_range("-456")==IS_INVALID_ID

def test_ids_invalid():
    assert check_id_range("123")==IS_INVALID_ID
    assert check_id_range("123-456-789")==IS_INVALID_ID
    assert check_id_range("")==IS_INVALID_ID

    assert check_id_range("123-")==IS_INVALID_ID

def test_id_valid():
    assert is_valid_id(123)
    assert is_valid_id(12)

def test_id_invalid():
    assert not is_valid_id(11)
    assert not is_valid_id(111)
    assert not is_valid_id(1212)
    assert not is_valid_id(5555)
