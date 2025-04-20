
def apply_case_option(word: str, case: str) -> str:
    if case == "lower":
        return word.lower()
    elif case == "upper":
        return word.upper()
    elif case == "nochange":
        return word
    else:
        raise ValueError(f"Invalid case option: {case}")
