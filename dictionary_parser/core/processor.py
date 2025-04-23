import csv
import json
from pathlib import Path
from typing import List, Dict

from dictionary_parser.utils.case import apply_case_option
from dictionary_parser.utils.validations import validate_letters


def process_words(
        words: List[str],
        letters: List[str],
        case: str,
        merge: bool,
        output_format: str,
        output_dir: Path,
        metadata_fields: List[str],
        use_local_index: bool = False,
        sort: bool = False,
) -> Dict[str, Dict[str, int]]:
    output_dir.mkdir(parents=True, exist_ok=True)
    data_by_letter = {}

    filtered_words = []
    global_index = 0
    loading = ''

    skipped_letters = 0
    print(f'Processing words per letter')
    for letter in letters:
        filtered = [w for w in words if w.lower().startswith(letter.lower())]
        if sort:
            filtered = sorted(filtered, key=lambda x: x.lower())
        processed = []
        for i, word in enumerate(filtered):
            if not validate_letters(word):
                skipped_letters += 1
                continue
            else:
                original = word.strip()
                transformed = apply_case_option(original, case)
                word_data = {"word": transformed}
                if "index" in metadata_fields:
                    if use_local_index:
                        # noinspection PyTypeChecker
                        word_data["index"] = i
                    else:
                        word_data["index"] = global_index + i
                if "length" in metadata_fields:
                    # noinspection PyTypeChecker
                    word_data["length"] = len(transformed)
                if "local_index" in metadata_fields:
                    # noinspection PyTypeChecker
                    word_data["local_index"] = i
                processed.append(word_data)

        if processed:
            if use_local_index:
                start_index = 0
                end_index = len(processed) - 1
            else:
                start_index = global_index
                end_index = global_index + len(processed) - 1

            data_by_letter[letter] = {
                "start_index": start_index,
                "end_index": end_index
            }
            global_index += len(processed)
            filtered_words.extend(processed)

            if not merge:
                loading += '.'
                print('\033[K', f'\rSaving files {loading}', end="\r", flush=True)
                save_data(processed, output_dir / f"{letter}.{output_format}", output_format)

    if merge:
        print('\033[K', f'Merging files', end='\r', flush=True)
        save_data(filtered_words, output_dir / f"filtered_words.{output_format}", output_format)

    if skipped_letters > 0:
        print(f'\033[K', f'\rSkipped {skipped_letters} word/s due to invalid characters', end="\r", flush=True)

    return data_by_letter


def save_data(data: List[Dict], output_file: Path, fmt: str) -> None:
    if fmt == "json":
        try:
            with output_file.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise ValueError(f"Error writing JSON file: {e}")
    elif fmt == "csv":
        try:
            with output_file.open("w", encoding="utf-8", newline="") as f:
                fieldnames = data[0].keys() if data else []
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            raise ValueError(f"Error writing CSV file: {e}")
    else:
        raise ValueError(f"Unsupported format: {fmt}")


def save_summary(summary: Dict[str, Dict[str, int]], output_file: Path, fmt: str) -> None:
    if fmt == "json":
        try:
            with output_file.open("w", encoding="utf-8") as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise ValueError(f"Error writing summary JSON file: {e}")
    elif fmt == "csv":
        try:
            with output_file.open("w", encoding="utf-8", newline="") as f:
                fieldnames = ["letter", "start_index", "end_index"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for letter, indices in summary.items():
                    writer.writerow({"letter": letter, **indices})
        except Exception as e:
            raise ValueError(f"Error writing summary CSV file: {e}")
    else:
        raise ValueError(f"Unsupported format: {fmt}")
