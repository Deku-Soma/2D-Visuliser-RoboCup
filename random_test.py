import pytest
import os

def test_gui_operation():
    if os.environ.get('DISPLAY') is None:
        pytest.skip("Skipping GUI test in headless environment")
        
from Display_menu_visualiser import add
def test_addition():
    result = add(2, 3)
    assert result == 5