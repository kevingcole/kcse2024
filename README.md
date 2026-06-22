# IT Asset System

This repository contains a Django-based IT asset management application.

## Requirements

- Python 3.10+
- pip

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run database migrations:

   ```bash
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Running checks

- Run tests:

  ```bash
  python manage.py test
  ```

- Run Django system checks:

  ```bash
  python manage.py check
  ```
