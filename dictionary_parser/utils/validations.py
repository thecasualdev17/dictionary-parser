import re

def validate_letters(letters: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9,-]*$", letters))