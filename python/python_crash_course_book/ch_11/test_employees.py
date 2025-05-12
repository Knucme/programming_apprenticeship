import pytest
from eleven_three_employee import Employees

@pytest.fixture
def employees():
    person = Employees('John', 'Doe', 95000)
    return person

def test_give_default_raise(employees):
    employees.give_raise()
    assert employees.salary == 100000

def test_give_custom_raise(employees):
    employees.give_raise(10000)
    assert employees.salary == 105000
