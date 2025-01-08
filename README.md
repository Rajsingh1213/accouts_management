# accouts_management

## Overview
**Account Management System** is a web application built with Django for managing personal or business finances.  
It allows users to:
- Register and securely log in.
- Add income and expense transactions.
- View an account summary showing total income, expenses, and current balance.
- Maintain a history of all transactions.

This project is suitable for anyone looking for an efficient financial management solution.


## Features

- **User Authentication**:
  - Register new users with a custom user model.
  - Login functionality with session-based authentication.
  - One active session per user to prevent simultaneous logins.

- **Financial Management**:
  - Add income and expense transactions.
  - Automatically calculate and display total income, expenses, and balance.
  - List all transactions in a detailed table.

- **User-Friendly Interface**:
  - Clean and responsive UI for login, registration, and dashboard pages.
  - Separate CSS files for each type of page for better customization.

- **API Endpoints**:
  - RESTful APIs for user authentication and transaction management.
 
### Prerequisites
- Python 3.12.4
- Django 5.1.4
- Virtual Environment (recommended)
 

### Steps

1. **Clone the repository**:
   git clone https://github.com/your-username/account-management-system.git
   cd account-management-system

2. **Create a virtual environment:**
   python -m venv venv
   source venv/bin/activate

3. **Create a virtual environment:**
   python -m venv venv
   source venv/bin/activate
   
5. **Install dependencies:**
   pip install -r requirements.txt

6. **Apply migrations:**
   python manage.py makemigrations
   python manage.py migrate

7. **Run the development server:**
   python manage.py runserver

8. **Access the application:**
   Open your browser and go to http://127.0.0.1:8000/

## Project Structure
myproject/ 
 ├── accounts/ │ 
 |       ├── migrations/ # Database migration files 
 |       ├── static/accounts/ # Static files (CSS)  
 |       ├── templates/accounts/ # HTML templates  
 |       ├── admin.py # Admin panel configuration  
 |       ├── apps.py # App configuration  
 |       ├── forms.py # Django forms for user operations  
 |       ├── models.py # Models (CustomUser, Transaction)  
 |       ├── urls.py # URLs for accounts app  
 |       ├── views.py # Views for pages and APIs 
 ├── myproject/ 
 |       ├── settings.py # Project settings  
 |       ├── urls.py # Root URL configuration 
 ├── db.sqlite3 # SQLite database 
 ├── manage.py # Django management script 
 ├── requirements.txt # Python dependencies 
 └── README.md # Project documentation

**Purpose**: Explain the workflows (e.g., login, transactions, etc.).

   User Authentication:
1. **Register**: Users can register with a username, password, and phone number.
2. **Login**: Users log in with valid credentials. Only one session per user is allowed.

   Transactions:
1. **Add Transaction**:
   - Input title, type (Income/Expense), and amount.
   - The dashboard updates totals and balance automatically.
2. **Dashboard**:
   - Displays total income, expenses, and balance.
   - Shows a table with all transaction details.
  
## API Documentation

   1. User Authentication
     **Register**: `POST /api/register/`
     **Login**: `POST /api/login/`

   2. Transactions
     **Add Transaction**: `POST /api/transactions/`
         Data: `{"title": "Salary", "amount": 10000, "transaction_type": "Income"}`
     **List Transactions**: `GET /api/transactions/`

9. Contributing:
     Purpose: Encourage others to contribute.

     Contributions are welcome! Follow these steps:
      1. Fork the repository.
      2. Create a feature branch:
         git checkout -b feature-branch-name 
   
      3. Commit your changes:
         git commit -m "Add some feature"

      4. Push the branch:
         git push origin feature-branch-name

      5. Open a pull request.


**License** 
    **Purpose**: Specify the project's license.
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

**Contact**
      Purpose: Allow users to reach out.

## Contact

      For questions or feedback, contact:

     Email: your-email@example.com  
     GitHub: [your-username](https://github.com/your-username)


