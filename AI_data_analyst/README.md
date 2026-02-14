# AI Data Analyst

CLI tool for data analysis with natural language queries.

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Load data
python main.py load data.csv

# Analyze
python main.py analyze

# Visualize
python main.py plot --type histogram --column age

# Query with AI
python main.py query "What is the average salary?"
```
