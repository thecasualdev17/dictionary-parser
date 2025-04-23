import sys
import typer
from pathlib import Path
from typing import Optional
import requests

from dictionary_parser.utils.letters import parse_letters
from dictionary_parser.core.processor import process_words

app = typer.Typer()


@app.command()
def generate(
        input_path: str,
        output_dir: Path,
        letters: Optional[str] = typer.Option(None, "--letters", "-l", help="Filter by letters: a, a-c, a,f"),
        case: str = typer.Option("nochange", "--case", "-c", help="Word casing: lower, upper, nochange"),
        format: str = typer.Option("json", "--format", "-f", help="Output format: json or csv"),
        merge: bool = typer.Option(False, "--merge", "-m", help="Export all data into one file"),
        metadata: Optional[str] = typer.Option(None,"--metadata", "-md",
            help="Comma-separated list of metadata fields to include: index, global_index, length"),

):
    print(f'Processing input_path to generate a {format} file.')
    words = ''
    if input_path.startswith("http"):
        print(f'Downloading file from {input_path}')
        response = requests.get(input_path)
        response.raise_for_status()
        words = response.text.strip().splitlines()
    else:
        print(f'Reading file from {input_path}')
        with open(input_path, "r", encoding="utf-8") as f:
            words = f.read().strip().splitlines()

    letter_list = parse_letters(letters)
    metadata_fields = metadata.split(",") if metadata else []
    process_words(words, letter_list, case, merge, format, output_dir, metadata_fields)
    print('\033[K', '\rFiles have been generated.', )
