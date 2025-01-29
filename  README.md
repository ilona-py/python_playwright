# Python Playwright Test Project

This project contains automated tests for the basic search functionality on [Kiwi.com](https://www.kiwi.com/en/) using Python, Playwright, Pytest, and BDD (Gherkin).

---

## **Project Structure**

```plaintext
python_playwright/
├── features/                  # Gherkin feature files
│   ├── basic_search.feature
├── pom/                       # Page Object Model files
│   ├── home_page_elements.py
├── tests/                     # Test files and step definitions
│   ├── conftest.py
│   ├── test_basic_search.py
├── pytest.ini                 # Pytest configuration file
├── requirements.txt           # Python dependencies
├── README.md                  # Instructions for setting up and running the tests
```

---

## **Prerequisites**

- **Python**: Version 3.9 or higher.
  - Ensure Python is installed. You can download it from [python.org](https://www.python.org/).
  - Verify the installation:
    ```bash
    python --version
    ```
- **pip**: Python package manager.
  - Usually installed with Python. Verify with:
    ```bash
    pip --version
    ```

---

## **Setup Instructions**

### 1. Install Dependencies
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 2. Install Playwright Browsers
Install the necessary browsers for Playwright:
```bash
playwright install
```

---

## **Running the Tests**

### 1. Run All Tests

To run all tests in the project, use:
```bash
pytest
```

### 2. Run a Specific Test Scenario

To run a specific test scenario:
```bash
pytest -m basic_search_one_way_flight
```

---

## **Troubleshooting**

### Problem: ModuleNotFoundError: No module named 'pom'

Solution: Ensure the project root is in the PYTHONPATH:
```bash
export PYTHONPATH=$(pwd)
```

---

## **Making the Script Work on a CI/CD Server**

To make this Playwright test project work on a CI/CD server, I have included an example Jenkins pipeline script in the file: `playwright-ci-pipeline.groovy`.

## **Additional Notes**
	•	Headless vs. Non-Headless Browsers:
	•	By default, tests run in a non-headless browser for debugging.
	•	Modify conftest.py to change headless=False to headless=True.

