import pytest

def test_sub():
    assert 2-2 == 0

@pytest.mark.smoke
def test_add():
    assert 2+2 != 3
@pytest.mark.reg
def test_div():
    assert 2/2 == 3
@pytest.mark.skip(reason="Not implemented")
def test_mul():
    assert 1*3 == 3