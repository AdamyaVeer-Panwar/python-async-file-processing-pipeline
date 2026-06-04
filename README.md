# Async File Processor

A production-inspired Python project demonstrating asynchronous file processing, validation, logging, exception handling, and automated testing.

A project that validates files, extracts metadata, reads files asynchronously, and returns structured processing results.

Built to practice software engineering concepts such as asynchronous programming, validation, testing, logging, exception handling, and clean architecture.

---

## Key Features

* File extension validation
* File size validation
* Metadata extraction
* Asynchronous file reading with `aiofiles`
* Structured logging
* Pydantic configuration validation
* Custom exception handling
* Processing result tracking
* Pytest test suite

---

## Why This Project?

Many Python projects focus only on getting code to work.

This project focuses on writing maintainable and scalable code by applying software engineering practices such as:

* Separation of concerns
* Configuration management
* Type safety
* Structured error handling
* Asynchronous I/O
* Automated testing
* Project organization

---

## System Workflow

```text
Input File
    │
    ▼
Validation
    │
    ├── Extension Check
    └── Size Check
    │
    ▼
Metadata Extraction
    │
    ▼
Async File Reading
    │
    ▼
Logging
    │
    ▼
ProcessingResult
```

---

## Project Structure

```text
async-file-processor/

├── data/
│
├── src/
│   ├── config.py
│   ├── exceptions.py
│   ├── logger.py
│   ├── main.py
│   ├── models.py
│   ├── processor.py
│   └── reader.py
│
├── tests/
│   ├── test_config.py
│   ├── test_reader.py
│   └── test_processor.py
│
└── pyproject.toml
```

---

## Technologies Used

| Technology  | Purpose                  |
| ----------- | ------------------------ |
| Python 3.10 | Core language            |
| asyncio     | Concurrency              |
| aiofiles    | Async file I/O           |
| pathlib     | File system operations   |
| pydantic    | Configuration validation |
| pytest      | Testing                  |
| logging     | Application logging      |

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd async-file-processor
```

Install dependencies:

```bash
pip install pydantic aiofiles pytest pytest-asyncio
```

---

## Usage

Create a `data` directory and place supported files inside it.

Example:

```text
data/
├── sample.txt
├── users.csv
```

Run the application:

```bash
python src/main.py
```

---

## Running Tests

Run all tests:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_processor.py -v
```

---

## Example Output

```text
data/sample.txt

2026-06-04 16:25:24,463 | INFO | async_file_processor | Successfully processed sample.txt

ProcessingResult(
    metadata=FileMetadata(
        filename='sample.txt',
        extension='.txt',
        size=16
    ),
    status=SUCCESS,
    error_message=None
)
```

---

## Engineering Concepts Demonstrated

* Asynchronous Programming
* Object-Oriented Design
* Dataclasses
* Enumerations
* Type Hints
* Exception Handling
* Structured Logging
* Configuration Validation
* Unit Testing
* Project Architecture

---

## Future Improvements

* Command Line Interface (CLI)
* JSON Logging
* Multiple File Format Support
* Directory Monitoring
* Performance Metrics
* Package Distribution
* Docker Support

---

## Author

Built as a software engineering learning project to practice production-oriented Python development patterns.
