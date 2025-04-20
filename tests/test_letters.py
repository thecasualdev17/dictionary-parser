
from dictionary_parser.utils.letters import parse_letters

def test_parse_letters_range():
    assert parse_letters("a-c") == ["a", "b", "c"]

def test_parse_letters_list():
    assert parse_letters("a,c,e") == ["a", "c", "e"]

def test_parse_letters_single():
    assert parse_letters("f") == ["f"]
