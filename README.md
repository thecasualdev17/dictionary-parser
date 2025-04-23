# 📘 Dictionary parser

**Dictionary parser** is a Python CLI tool for processing and exporting dictionary word lists with customizable filters, formats, and casing options.  
Perfect for building vocabulary apps, language tools, or educational datasets.

[![PyPI version](https://badge.fury.io/py/dictionary-parser.svg)](https://badge.fury.io/py/dictionary-parser)
[![Builds and Tests](https://github.com/thecasualdev17/dictionary-parser/actions/workflows/python-build-test.yml/badge.svg?branch=main)](https://github.com/thecasualdev17/dictionary-parser/actions/workflows/python-build-test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🔧 Features

- ✅ Filter words by starting letter or letter range (`a`, `a-c`, `a,c,f`)
- ✅ Export as JSON or CSV
- ✅ Convert word case: `lower`, `upper`, or no change
- ✅ Output to one file or split by starting letter
- ✅ Works with local files or download from a URL
- ✅ Fast and clean CLI powered by [Typer](https://typer.tiangolo.com)
- ✅ Metadata support: `local_index`, `length`
- ✅ Sort words in the output files
- ✅ Use local index per letter instead of global index

---

## 🚀 Installation

Install via pip:

```bash
pip install dictionary-parser
```

## 🧪 Quick Usage

```bash
dictionary-parser input.txt output/ --letters=a-c --format=csv --case=lower
```
### Arguments:
 - input.txt — your source word list file
 - output/ — directory for saving results

### Options:

| Option            | Description                                                             |
|-------------------|-------------------------------------------------------------------------|
| --letters         | Letter filter: a, a-c, or a,c,f                                         |
| --format          | Output format: json (default) or csv                                    |
| --case            | Word casing: lower, upper, or nochange (default)                        |
| --merge           | Export all data into one file instead of per-letter files               |
| --metadata        | Comma-separated list of metadata fields to include: local_index, length |
| --use-local-index | Use local index per letter instead of global index                      |
| --sort            | Sort words in the output files                                          |
| --help            | Show help message and exit                                              |

## 🔍 Examples
Only export words starting with A, B, or C in lowercase CSV:

```bash
dictionary-parser input.txt output/ --letters=a-c --format=csv --case=lower
```

Export only A and F in JSON to a single file:
```bash
dictionary-parser input.txt output/ --letters=a,f --merge
```

## 📂 Directory Structure

```graphql

dictionary-parser/
├── dictionary-parser/       # Main CLI app folder
├── docs/                       # Docs Folder
├── tests/                      # Pytest unit tests

```

## 📚 Documentation

Full documentation available at: https://dictionary-parser.readthedocs.io

## 🧑‍💻 Contributing

We love contributions! See our CONTRIBUTING.md for how to get started.

## 📜 License

This project is licensed under the MIT License.

## ❤️ Credits

Built with Typer and Python.