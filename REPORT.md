# PubMed Company Affiliation Analysis - Project Report

## Overview
This project implements a tool to analyze research papers from PubMed and identify those with pharmaceutical/biotech company affiliations. The tool helps track industry involvement in academic research by analyzing author affiliations.

## Approach

### 1. Data Source
- **PubMed API**: Used Biopython's Entrez interface to access PubMed's extensive database
- **Query System**: Implemented support for PubMed's full query syntax
- **Batch Processing**: Implemented efficient batch fetching to handle large result sets

### 2. Company Affiliation Detection
Developed a sophisticated two-step detection system:

1. **Company Keyword Detection**:
   - Comprehensive list of company indicators (e.g., 'Inc', 'Corp', 'Ltd')
   - Industry-specific terms (e.g., 'Pharma', 'Biotech', 'Therapeutics')
   - International company types (e.g., 'GmbH', 'AG', 'BV')

2. **Academic Exclusion**:
   - Filters out academic/healthcare institutions
   - Keywords include: universities, hospitals, research centers
   - Handles international variations and abbreviations

### 3. Technical Implementation

#### Architecture
- **Modular Design**:
  - Core PubMed interaction module
  - Data models for Authors and Papers
  - CLI interface for easy access
  - Jupyter notebook for interactive analysis

#### Key Features
- Type-annotated Python code
- Efficient batch processing
- Comprehensive error handling
- CSV export functionality
- Interactive Jupyter interface

## Methodology

### Data Processing Pipeline
1. **Query Execution**:
   - Submit search query to PubMed
   - Retrieve paper IDs in batches
   
2. **Paper Processing**:
   - Fetch detailed records for each paper
   - Parse author information and affiliations
   
3. **Affiliation Analysis**:
   - Extract and normalize affiliations
   - Apply company detection algorithm
   - Filter non-academic affiliations

### Affiliation Detection Algorithm
```python
def has_company_affiliation(affiliation):
    1. Convert to lowercase
    2. Split into words
    3. Check for company keywords
    4. Verify absence of academic keywords
    5. Return True if company-affiliated
```

## Results

### Performance Metrics
- Successfully identifies company affiliations with high accuracy
- Handles various affiliation formats
- Processes large result sets efficiently

### Example Output
```
PubMed ID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s)
---------|-------|------------------|----------------------|---------------------
39435256 | AI in Healthcare | 2023-01-01 | John Doe | Pfizer Inc., NY
```

### Key Findings
1. Successfully detects various company types:
   - Pharmaceutical companies
   - Biotech firms
   - Research corporations

2. Handles edge cases:
   - Mixed affiliations
   - International institutions
   - Complex organizational structures

## Technical Details

### Dependencies
- Python 3.9+
- Biopython for PubMed API
- Pandas for data handling
- Typer for CLI
- Rich for terminal output

### Installation
```bash
poetry install
```

### Usage
```bash
poetry run get-papers-list "your query" [options]
```

## Future Improvements

1. **Enhanced Detection**:
   - Machine learning for affiliation classification
   - Natural language processing for context understanding
   - Expanded keyword databases

2. **Additional Features**:
   - Citation analysis
   - Collaboration network visualization
   - Historical trend analysis

3. **Performance Optimization**:
   - Caching frequently accessed data
   - Parallel processing for large queries
   - Memory optimization for large datasets

## Conclusion
The tool successfully achieves its goal of identifying company-affiliated research papers in PubMed. It provides a robust foundation for analyzing industry involvement in academic research, with room for future enhancements and expansions. 