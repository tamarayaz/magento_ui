#  magento_ui / UI Test Automation project (Selenium)
This project is a UI test automation framework built with Python, Selenium, and Pytest.  
It covers core user flows of an e-commerce demo website using the Page Object Model (POM) design pattern.

## What is tested
- Account registration functionality
- Form validation and error messages
- Product selection (size & color)
- Add to cart functionality
- Navigation between sale categories
- Page titles and URLs validation

## Test scenarios

### Positive scenarios
- Successful account registration
- Adding product to cart with selected options
- Navigation to Women and Men deals pages
- Sale page displays product items

### Negative scenarios
- Empty required registration fields
- Password mismatch validation
- Attempt to add product without selecting required options

Tests are grouped using pytest markers:
- `smoke`
- `regression`
- `navigation`

## How to Run Tests

```bash
pip install -r requirements.txt
pytest
```
Run specific test groups:
```bash
pytest -m smoke
pytest -m regression
pytest -m navigation
```

## Tech Stack

- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- GitHub Actions (CI)
