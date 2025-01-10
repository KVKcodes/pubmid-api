# PubMed Papers

A Python tool to fetch research papers from PubMed and identify those with pharmaceutical/biotech company affiliations.

## Installation

1. Make sure you have Python 3.9+ and Poetry installed
2. Clone this repository
3. Install dependencies:
```bash
poetry install
```

## Usage

Basic command structure:
```bash
poetry run get-papers-list "your search query" [options]
```

Options:
- `-h, --help`: Show help message
- `-d, --debug`: Enable debug logging
- `-f, --file`: Specify output CSV file (defaults to console output)
- `-t, --test`: Test mode: only fetch first 10 papers

## Example Queries

### 1. Company-Specific Searches
```bash
# Papers from specific companies
poetry run get-papers-list "pfizer[ad]" -f pfizer_papers.csv

# Multiple companies
poetry run get-papers-list "(moderna[ad] OR pfizer[ad] OR novartis[ad])" -f companies.csv

# Company papers from specific year
poetry run get-papers-list "pfizer[ad] AND 2023[dp]" -f pfizer_2023.csv
```

### 2. Research Area Searches
```bash
# Industry cancer research
poetry run get-papers-list "(pharmaceutical[ad] OR biotech[ad]) AND cancer" -f cancer_industry.csv

# COVID-19 industry papers
poetry run get-papers-list "(company[ad] OR inc[ad] OR corp[ad]) AND covid-19" -f covid_industry.csv

# Recent clinical trials
poetry run get-papers-list "(pharmaceutical[ad] OR biotech[ad]) AND \"clinical trial\"[pt] AND 2023[dp]"
```

### 3. Advanced Queries
```bash
# Papers with company affiliations in specific journals
poetry run get-papers-list "(corp[ad] OR inc[ad]) AND \"Nature\"[journal]"

# Industry papers with specific keywords in title
poetry run get-papers-list "(pharmaceutical[ad] OR biotech[ad]) AND immunotherapy[ti]"

# Papers with company authors as first author
poetry run get-papers-list "(inc[ad] OR corp[ad]) AND \"first author\""
```

### 4. Test Mode Examples
```bash
# Test a query with limited results
poetry run get-papers-list "cancer immunotherapy" --test

# Debug mode with test query
poetry run get-papers-list "pfizer[ad]" --test --debug
```

## Output Format

The tool generates a CSV with the following columns:
- PubMed ID
- Title
- Publication Date
- Non-academic Author(s)
- Company Affiliation(s)
- Corresponding Author Email

## Development

This project uses:
- Type hints throughout the codebase
- Black for code formatting
- MyPy for type checking
- isort for import sorting

## License

MIT 