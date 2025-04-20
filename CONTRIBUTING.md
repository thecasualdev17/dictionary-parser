# Contributing to Dictionary parser

🎉 Thank you for your interest in contributing to Dictionary parser!  
We welcome all contributions—bug reports, feature requests, documentation, and code.

## 🛠️ How to Contribute

### 1. Fork the Repository

Click the **Fork** button in the top-right corner of the [GitHub repo](https://github.com/thecasualdev17/dictionary_parser) and clone your fork locally:

```bash
git clone https://github.com/thecasualdev17/dictionary_parser.git
cd dictionary-parser
```
### 2. Set Up Your Environment
Make sure you have python 3.9+ and install the dependencies:

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -e . (dev)
```

### 3. Create a Branch
Use descriptive names like fix-case-handling or feature-letter-range-support.

```bash
git checkout -b feature-your-description
```

### 4. Make your changes
 - Code style: follow [PEP 8](https://pep8.org/)
 - Document new changes and update the CLI help text if needed
 - Include or update unit tests in tests/

### 5. Run Tests

```bash
pytest
```

### 6. Commit and Push
Write clear and concise commit messages.
```bash
git add .
git commit -m "Add new CLI option --letters"
git push origin feature-your-description
```

### 7. Open a Pull Request
Go to the repository and open a PR from your branch to main. 
Describe:
 - What you changed
 - Why it matters
 - Any dependencies or follow-up work

## Running the CLI locally
Example usage from your local checkout:
```bash
python -m core.cli generate examples/input.txt output/ --letters=a-c --case=upper
```

## ✅ Good First Issues

Check out the [Issues](https://github.com/thecasualdev17/dictionary_parser/issues) tab for labels like good first issue and help wanted.

## 💬 Community & Help

Feel free to ask questions by opening a discussion or [issue](https://github.com/thecasualdev17/dictionary_parser/issues).

## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
You can also share your best practices with us.
