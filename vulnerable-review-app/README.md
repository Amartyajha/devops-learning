# Vulnerable Review App

This is a deliberately vulnerable Flask application designed to test AI code review tools. It contains various code quality and security issues for evaluation purposes.

**WARNING: This application contains intentional vulnerabilities. DO NOT use in production!**

## Intentional Issues Included

### Code Quality Issues

1. Performance Issues:
   - Unnecessary computations in loops
   - Inefficient data structure usage (list vs set)
   - Suboptimal pandas/numpy operations
   - Redundant type conversions

2. Dead Code:
   - Unused imports
   - Unreachable functions
   - Unnecessary variables

3. Anti-patterns:
   - Global mutable state
   - Redundant data transformations
   - Poor error handling

4. Business Logic Errors:
   - Incorrect discount calculation
   - Flawed data processing logic

### Security Issues

1. Static Application Security:
   - SQL Injection vulnerability
   - Command Injection vulnerability
   - XML parsing vulnerability (XXE)
   - Insecure password hashing (MD5)

2. Configuration Issues:
   - Debug mode enabled in production
   - Hardcoded credentials
   - Insecure database configuration

3. Dependency Issues:
   - Outdated package versions with known vulnerabilities
   - Insecure defaults

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```

4. Run the application:
```bash
python app.py
```

## Note

This application is designed for testing code review tools. It contains deliberate vulnerabilities and should never be used in a production environment.
