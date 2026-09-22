# KVD Insurance Group QA Automation

Public QA portfolio project for testing the KVD Insurance Group web application.

## Current scope

- Manual QA test plan
- Smoke testing with Python + pytest + requests
- API testing (next)
- UI automation with Playwright (later)
- CI with GitHub Actions (later)

## Setup

1. Create a Python virtual environment:

   ```bash
   python -m venv .venv
   ```

2. Activate it:

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set the URL of the KVD site you want to test:

   macOS/Linux:

   ```bash
   export KVD_BASE_URL="https://your-kvd-site.com"
   ```

   Windows PowerShell:

   ```powershell
   $env:KVD_BASE_URL="https://your-kvd-site.com"
   ```

5. Run the tests:

   ```bash
   pytest -v
   ```

## First automated test

`tests/test_smoke.py` checks that the configured KVD homepage:

- is reachable
- returns HTTP 200
- contains the expected `KVD Insurance` text

The base URL is intentionally configurable so the same test suite can target a local, staging, or deployed version of the application without hard-coding a production URL.
