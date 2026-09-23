# KVD QA Automation

Automated QA tests for the KVD Insurance website and quote API.

## Current Coverage

- Homepage smoke test
- Malformed JSON API validation
- Required quote field validation
- Production and localhost testing

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Tests

Run against production:

```bash
pytest -v
```

Run against local development:

```bash
KVD_BASE_URL=http://localhost:3000 pytest -v
```

## Project Structure

```text
tests/
  test_smoke.py
  test_quote_api.py

bug_reports/
  BUG-001-malformed-json-returns-500.md
```

## Configuration

The test suite uses the `KVD_BASE_URL` environment variable when provided.

If no environment variable is set, the tests default to:

```text
https://kvdinsurance.com
```

## Purpose

This project is used to practice and demonstrate QA workflows including:

- Functional testing
- API testing
- Negative testing
- Regression testing
- Bug reporting
- Local vs production verification
- Git branching and pull request workflows