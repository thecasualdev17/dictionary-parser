def parse_letters(input_str: str):
    if not input_str:
        return [chr(i) for i in range(ord('a'), ord('z') + 1)]

    letters = set()
    parts = input_str.split(",")

    for part in parts:
        if "-" in part:
            start, end = part.split("-")
            for i in range(ord(start.lower()), ord(end.lower()) + 1):
                letters.add(chr(i))
        else:
            letters.add(part.lower())

    return sorted(letters)
