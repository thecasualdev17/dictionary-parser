import typer
from pathlib import Path
from typing import Optional
import requests

from dictionary_parser.utils.letters import parse_letters
from dictionary_parser.core.processor import process_words, save_summary

app = typer.Typer()

@app.command()
def generate(
        input_path: str,
        output_dir: Path,
        letters: Optional[str] = typer.Option(None, "--letters", "-l", help="Filter by letters: a, a-c, a,f"),
        case: str = typer.Option("nochange", "--case", "-c", help="Word casing: lower, upper, nochange"),
        format: str = typer.Option("json", "--format", "-f", help="Output format: json or csv"),
        merge: bool = typer.Option(False, "--merge", "-m", help="Export all data into one file"),
        metadata: Optional[str] = typer.Option(None, "--metadata", "-md",
                                               help="Comma-separated list of metadata fields to include: local_index, length"),
        use_local_index: bool = typer.Option(False, "--use-local-index",
                                             help="Use local index instead of global index"),
        sort: bool = typer.Option(False, "--sort", "-s", help="Sort words alphabetically"),
):
    print(f'Processing')
    words = ''
    if input_path.startswith("http"):
        print(f'Downloading file')
        response = requests.get(input_path)
        response.raise_for_status()
        words = response.text.strip().splitlines()
    else:
        print(f'Reading file')
        try:
            with open(input_path, "r", encoding="utf-8") as f:
                words = f.read().strip().splitlines()
        except FileNotFoundError:
            raise ValueError(f"Input file not found:")
        except Exception as e:
            raise ValueError(f"Error reading file: {e}")

    letter_list = parse_letters(letters)
    metadata_fields = metadata.split(",") if metadata else []
    metadata_fields.insert(0, "index")
    data_by_letter = process_words(words, letter_list, case, merge, format, output_dir, metadata_fields,
                                   use_local_index, sort)
    summary_file = output_dir / f"summary.{format}"
    save_summary(data_by_letter, summary_file, format)
    print()
    print('\033[K', '\rFiles have been generated.', )
