# CUCUMBER-JS + CYPRESS

1. https://docs.cypress.io/guides/guides/command-line
2. https://docs.cypress.io/guides/references/configuration#Folders-Files

# CUCUMBER + SELENIUM + SPLINTER

## Behave
```bash
behave features/e2e/ya.feature
```

## Pytest + Pytest-bdd
```bash
pytest features/e2e/ya.py
```
### Pytest start with logger
```bash
pytest -s features/e2e/ya.py
```
### Generate test py
```bash
pytest-bdd generate features/e2e/ya.feature > features/e2e/ya.py 
```

### Install
```bash
pip install pytest-splinter
```