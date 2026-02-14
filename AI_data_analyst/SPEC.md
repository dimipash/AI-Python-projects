# AI Data Analyst - Specification

## Project Overview
- **Name**: AI Data Analyst
- **Type**: CLI tool with optional web interface
- **Core Functionality**: Load data files, analyze with pandas, generate visualizations, answer questions via LLM
- **Target Users**: Developers, data analysts, researchers needing quick data insights

## Features

### 1. Data Loading
- Support CSV files
- Support Excel files (.xlsx, .xls)
- Auto-detect delimiters for CSV
- Handle encoding issues

### 2. Data Analysis
- Column statistics (count, unique, nulls, mean, median, std, min, max)
- Data types detection
- Correlation matrix for numeric columns
- Basic data profiling

### 3. Visualizations
- Histograms for numeric columns
- Bar charts for categorical columns
- Correlation heatmap
- Save plots as PNG

### 4. LLM Integration
- Natural language queries about data
- Uses OpenAI GPT-4o mini (cost-effective)
- Context-aware responses based on loaded data

### 5. CLI Interface
- Load file: `python main.py load data.csv`
- Analyze: `python main.py analyze`
- Visualize: `python main.py plot --type histogram --column age`
- Query: `python main.py query "What is the average age?"`

## Technical Stack
- Python 3.13+
- pandas - data manipulation
- matplotlib/seaborn - visualizations
- openai - LLM integration
- python-dotenv - env variables
- click - CLI framework
- pyarrow / openpyxl - Excel support

## Project Structure
```
AI_data_analyst/
├── pyproject.toml
├── main.py
├── .env.example
├── src/
│   ├── __init__.py
│   ├── loader.py      # Data loading
│   ├── analyzer.py    # Statistical analysis
│   ├── visualizer.py  # Plot generation
│   ├── query.py       # LLM queries
│   └── cli.py         # CLI commands
└── outputs/           # Generated plots
```

## Acceptance Criteria
1. Can load CSV and Excel files successfully
2. Provides column statistics on demand
3. Generates and saves visualizations
4. Answers natural language questions about data
5. Works entirely offline for stats/plots (LLM optional)
