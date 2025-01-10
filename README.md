# PubMed Papers

A Python tool to fetch research papers from PubMed and identify those with pharmaceutical/biotech company affiliations.

Made for internship assignment

## Features

- Search PubMed using full query syntax
- Filter papers by author affiliations
- Export results to CSV
- Command-line interface with various options
- Type-annotated Python code
- Comprehensive error handling

## Installation

1. Make sure you have Python 3.9+ and Poetry installed
2. Clone this repository
3. Install dependencies:
```bash
poetry install
```

## Usage

The tool can be used via the command line:

```bash
poetry run get-papers-list "your search query" [options]
```

Options:
- `-h, --help`: Show help message
- `-d, --debug`: Enable debug logging
- `-f, --file`: Specify output CSV file (defaults to console output)
- `-t, --test`: Test mode: only fetch first 10 papers
Example:
```bash
poetry run get-papers-list "pharm" -f results.csv
```

## Output Format

The tool generates a CSV with the following columns:
- PubMed ID
- Title
- Publication Date
- Non-academic Author(s)
- Company Affiliation(s)
- Corresponding Author Email

## Project Structure

```
pubmed_papers/
├── __init__.py
├── cli.py           # Command-line interface
├── core.py          # Core functionality
├── models.py        # Data models
└── utils.py         # Utility functions
```

## Tools Used

- [Poetry](https://python-poetry.org/) - Dependency management
- [Typer](https://typer.tiangolo.com/) - CLI interface
- [Biopython](https://biopython.org/) - PubMed API interaction
- [Pandas](https://pandas.pydata.org/) - Data processing
- [Rich](https://rich.readthedocs.io/) - Terminal output formatting
- [Claude](https://www.anthropic.com/en/claude) - AI assistant

## Development

This project uses:
- Type hints throughout the codebase
- Black for code formatting
- MyPy for type checking
- isort for import sorting
