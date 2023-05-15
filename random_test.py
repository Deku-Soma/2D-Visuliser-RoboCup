import pytest
from Display_menu_visualiser import add
def test_addition():
    result = add(2, 3)
    assert result == 5