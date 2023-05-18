import pytest
import os
from Display_menu_visualiser import add

@pytest.mark.skipif(os.environ.get('DISPLAY') is None, reason="Skipping GUI test in headless environment")
def test_gui_operation():
    # Rest of the test code involving GUI operations
    # ...
    # ...
    def test_addition():
        result = add(2, 3)
        assert result == 5



