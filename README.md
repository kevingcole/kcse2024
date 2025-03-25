# Team IT Asset System

## Overview

The Team IT Asset System is a web application designed to manage IT assets within an organization. It allows users to register, log in, and manage IT assets, including adding, updating, and deleting assets. The system also provides user profile management and asset assignment features.

## Features

- User Registration and Authentication
- User Profile Management
- IT Asset Management
  - Add new assets
  - Update existing assets
  - Delete assets
  - View asset details
- Asset Assignment to Employees
- Pagination for asset lists
- Responsive design with Bootstrap
- Font Awesome icons for enhanced UI

## Technologies Used

- Python
- Django
- Bootstrap
- Font Awesome
- SQLite (default database)

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:kevingcole/kcse2024.git
   cd kcse2024

2. **Create & Activate a virtual environment**

    python3 -m venv venv
    source venv/bin/activate

3. **Install the required packages**

    pip install -r requirements.txt

4. **Apply Migrations**

    python manage.py migrate

5. **Create a superuser**

    python manage.py createsuperuser

6. **Run the development server**

    python manage.py runserver

7.  **Access the application**

    Open your web browser and go to http://127.0.0.1:8000/.

**Usage**
    Register a new user:

    Go to the registration page and create a new account.

Log in:

    Use your credentials to log in to the system.

Manage IT assets:

    Add new assets by navigating to the "Add Asset" page.
    View asset details by clicking on the magnifying glass icon next to each asset.
    Update or delete assets from the asset detail page.
    Manage user profile:

    View and update your profile information from the profile page.
    Change your password from the profile page.

Contributing

    Contributions are welcome! Please fork the repository and create a pull request with your changes.

License

    This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For any questions or enquiries, please contact Kevin Cole at kev@kevcoleit.co.uk


