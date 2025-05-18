# E-commerce Test Automation

This project contains automated API and UI tests for a sample e-commerce application using Python.

## Features
- **API Testing** using `requests` for product listing and validation
- **UI Testing** using `selenium` on a mock login HTML page
- **Modular and Scalable Code Structure**
- **Beginner-friendly**, ready for CI/CD integration

## Project Structure
- `api_tests/`: Contains API test cases
- `ui_tests/`: Contains UI test cases and mock HTML
- `utils/`: Config and helper base classes

## How to Run

1. **Install dependencies:**
```
pip install -r requirements.txt
```

2. **Run API Tests:**
```
python -m unittest api_tests/test_products_api.py
```

3. **Run UI Tests (uses mock_login.html):**
```
python -m unittest ui_tests/test_login_ui.py
```

> *Make sure ChromeDriver is installed and available in your system PATH.*

---

## Notes:
- The UI tests use a **local mock login page (mock_login.html)**.
- No real credentials or external pages are used, making it ideal for test demonstration.
