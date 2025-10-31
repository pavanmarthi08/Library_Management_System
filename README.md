# Library Management System (Python CLI)

A command-line library management system supporting:
- Book management (add, edit, find, list)
- Member management (add, edit, find, list)
- Transactions (issue/return books)
- Reports (status, search, lists)

## Usage

```bash
python library.py
```

All data is stored in `books.json`, `members.json`, and `transactions.json`.

## Project Structure

- `library.py` — Main menu and navigation
- `books.py` — Book operations
- `members.py` — Member operations
- `transactions.py` — Issue/return operations and status
- `utils.py` — Helper functions
