
import sys
import csv
import json
from pathlib import Path
from turtledemo.penrose import start
from typing import List, Dict

from dictionary_parser.utils.case import apply_case_option


def process_words(
    words: List[str],
    letters: List[str],
    case: str,
    merge: bool,
    output_format: str,
    output_dir: Path,
) -> Dict[str, Dict[str, int]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    data_by_letter = {}

    filtered_words = []
    global_index = 0

    print('Processing')
    for letter in letters:
        print(f'Looking for words starting with letter {letter}', end="\r", flush=True)
        filtered = [w for w in words if w.lower().startswith(letter.lower())]
        processed = []
        for i, word in enumerate(filtered):
            original = word.strip()
            transformed = apply_case_option(original, case)
            processed.append({
                "word": transformed,
                "index": i,
                "length": len(transformed),
                "global_index": global_index + i
            })
        if processed:
            data_by_letter[letter] = {
                "start_index": global_index,
                "end_index": global_index + len(processed) - 1
            }
            global_index += len(processed)
            filtered_words.extend(processed)

            if not merge:
                print('\033[K', f'\rSaving {letter}.{output_format} file', end="\r", flush=True)
                save_data(processed, output_dir / f"{letter}.{output_format}", output_format)

    if merge:
        print('\033[K', f'Merging to {output_format} file', end='\r', flush=True)
        save_data(filtered_words, output_dir / f"filtered_words.{output_format}", output_format)

    return data_by_letter


def save_data(data: List[Dict], output_file: Path, fmt: str) -> None:
    if fmt == "json":
        with output_file.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    elif fmt == "csv":
        with output_file.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["word", "index", "length", "global_index"])
            writer.writeheader()
            writer.writerows(data)
    else:
        raise ValueError(f"Unsupported format: {fmt}")
