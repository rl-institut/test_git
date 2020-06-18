from src.A1 import variable_in_src_A1
from mvs_eland_tool import main

def test_import_package():
    assert variable_in_src_A1 < main()
