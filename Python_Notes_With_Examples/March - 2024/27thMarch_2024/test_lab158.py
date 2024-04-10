#Fixture (important concept in Python) , pytest
#You can use fixtures in -> 1. Setup, provide any data, teardown resource in your Testcases,
#pass some of the data to other test cases you can use the fixture.
import pytest
@pytest.fixture #inbuild feature of python we can use on another test case also
def sample_test():
    data = [1,2,3,4,5,6] #type --> list
    return data
#only fixtures can be passed to test cases , test cases cant be passed to
# another test cases
@pytest.fixture
def sample_test2():
    return True
def test_sample_data(sample_test):
    assert len(sample_test) == 6
def test_sample_data2(sample_test,sample_test2):
    assert sample_test2 == True
    assert 3 in sample_test
#instead of calling the function we can use pytest. fixture to call the function
"""def test_number1_sample_test():
    data2 = sample_test()
    assert len(data2) == 5"""