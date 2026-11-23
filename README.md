
# Personal Finance Tracker

A command-line application for managing personal finances, built with Python.

The project allows users to track income and expenses, manage transactions, generate financial reports, and export data to CSV.

## Features

- Add income and expenses
- Edit and delete transactions
- View transaction history
- Calculate current balance
- Summarize expenses by category
- Generate monthly financial reports
- Filter transactions by type, category, and date range
- Save and load transactions using JSON
- Export transactions to CSV
- Validate transaction data
- Automated tests using pytest

## Technologies

- **Python 3** - Application development
- **JSON** - Local data storage
- **CSV** - Transaction export
- **pytest** - Automated testing
- **Git** - Version control
- **GitHub** - Source code hosting

## Requirements

- Python 3
- Git (for cloning the repository)
- pytest (for running automated tests)

The application uses Python's standard library and does not require additional third-party packages to run.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/dkrupski/personal-finance-tracker.git
cd personal-finance-tracker
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On Linux or macOS:

```bash
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install pytest

```bash
python -m pip install pytest
```

## Usage

Run the application:

```bash
python main.py
```

The application provides an interactive command-line menu for managing personal finances.

Users can add, edit, delete, and filter transactions, view financial summaries, and generate reports.

## Running Tests

The project includes automated tests written with pytest.

Run all tests:

```bash
python -m pytest -v
```

The test suite covers:

- Expense summaries
- Monthly financial reports
- Transaction filtering
- JSON data saving and loading
- Invalid JSON handling
- Adding income transactions

## Project Structure

```text
personal-finance-tracker/
├── main.py
├── transactions.py
├── reports.py
├── storage.py
├── tests/
│   ├── test_reports.py
│   ├── test_storage.py
│   └── test_transactions.py
├── .gitignore
└── README.md
```

### Module Description

| File | Description |
|------|-------------|
| `main.py` | Application entry point and interactive menu |
| `transactions.py` | Adding, editing, and deleting transactions |
| `reports.py` | Financial reports, summaries, and filtering |
| `storage.py` | JSON data storage and CSV export |
| `tests/` | Automated tests using pytest |

## Data Storage

Transactions are stored locally in `transakcje.json`.

The application uses a temporary file (`transakcje.tmp`) and an atomic file replacement operation to reduce the risk of data corruption during saving.

Transaction data can also be exported to `eksport_transakcji.csv`.

These generated data files are excluded from Git version control using `.gitignore`.

## Error Handling

The application includes basic error handling and data validation.

- Transaction amounts must be positive numbers.
- Transaction data is validated when loading JSON files.
- Missing JSON files are handled automatically.
- Invalid or corrupted JSON files are detected.
- Failed save operations are reported to the user.

## Project Purpose

This project was created to develop practical Python programming skills, including:

- Functions and modules
- Lists and dictionaries
- File handling
- JSON and CSV processing
- Input validation
- Exception handling
- Automated testing
- Git and GitHub workflows


## Author

GitHub: [dkrupski](https://github.com/dkrupski)

