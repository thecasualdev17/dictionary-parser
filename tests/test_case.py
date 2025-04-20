
from dictionary_parser.utils.case import apply_case_option

def test_apply_case_option():
    assert apply_case_option("Test", "lower") == "test"
    assert apply_case_option("Test", "upper") == "TEST"
    assert apply_case_option("Test", "nochange") == "Test"
