# Daily Expenses Sharing Application

## Introduction

This application is designed to manage and share daily expenses among multiple users. Users can add expenses and split them using three different methods: equal amounts, exact amounts, and percentages. The application also supports downloading the balance sheet as a CSV file.

## Features

- **User Management**: Each user has an email, name, and mobile number.
- **Expense Management**: Users can add expenses and split them using equal, exact, or percentage methods.
- **Balance Sheet**: Display individual and overall balances for all users.
- **Download Balance Sheet**: Export the balance sheet as a CSV file.

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/daily-expenses-sharing-app.git
    cd daily-expenses-sharing-app
    ```

2. Install the required packages:
    ```bash
    pip install flask
    ```

3. Run the application:
    ```bash
    python app.py
    ```

## API Endpoints

### User Endpoints

#### Create User

- **Endpoint**: `/user`
- **Method**: `POST`
- **Payload**:
    ```json
    {
        "name": "John",
        "email": "john@example.com",
        "mobile": "1234567890"
    }
    ```

- **Example Command**:
    ```bash
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"John\", \"email\": \"john@example.com\", \"mobile\": \"1234567890\"}"
    ```

#### Retrieve User Details

- **Endpoint**: `/user/<name>`
- **Method**: `GET`
- **Example Command**:
    ```bash
    curl http://127.0.0.1:5000/user/john
    ```

### Expense Endpoints

#### Add Expense

- **Endpoint**: `/expense`
- **Method**: `POST`
- **Payload**:
    ```json
    {
        "description": "Dinner",
        "amount": 100,
        "paid_by": "john",
        "splits": {
            "john": 50,
            "doe": 50
        }
    }
    ```

- **Example Command**:
    ```bash
    curl -X POST http://127.0.0.1:5000/expense -H "Content-Type: application/json" -d "{\"description\": \"Dinner\", \"amount\": 100, \"paid_by\": \"john\", \"splits\": {\"john\": 50, \"doe\": 50}}"
    ```

#### Retrieve Overall Balances

- **Endpoint**: `/balances`
- **Method**: `GET`
- **Example Command**:
    ```bash
    curl http://127.0.0.1:5000/balances
    ```

#### Generate Balance Sheet

- **Endpoint**: `/balance-sheet`
- **Method**: `GET`
- **Example Command**:
    ```bash
    curl http://127.0.0.1:5000/balance-sheet
    ```

#### Download Balance Sheet

- **Endpoint**: `/download-balance-sheet`
- **Method**: `GET`
- **Example Command**:
    ```bash
    curl http://127.0.0.1:5000/download-balance-sheet -o balance_sheet.csv
    ```

## Example Scenarios

### 1. Equal Split

#### Scenario:
You go out with 3 friends. The total bill is 3000. Each friend owes 750.

#### Steps:

1. **Add Users**:
    ```bash
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Alice\", \"email\": \"alice@example.com\", \"mobile\": \"1234567890\"}"
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Bob\", \"email\": \"bob@example.com\", \"mobile\": \"0987654321\"}"
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Charlie\", \"email\": \"charlie@example.com\", \"mobile\": \"1122334455\"}"
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Dave\", \"email\": \"dave@example.com\", \"mobile\": \"5566778899\"}"
    ```

2. **Add Expense** (Equal Split):
    ```bash
    curl -X POST http://127.0.0.1:5000/expense -H "Content-Type: application/json" -d "{\"description\": \"Dinner\", \"amount\": 3000, \"paid_by\": \"alice\", \"splits\": {\"alice\": 750, \"bob\": 750, \"charlie\": 750, \"dave\": 750}}"
    ```

3. **Get Balances**:
    ```bash
    curl http://127.0.0.1:5000/balances
    ```

4. **Generate Balance Sheet**:
    ```bash
    curl http://127.0.0.1:5000/balance-sheet
    ```

### 2. Exact Split

#### Scenario:
You go shopping with 2 friends and pay 4299. Friend 1 owes 799, Friend 2 owes 2000, and you owe 1500.

#### Steps:

1. **Add Users**:
    ```bash
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"John\", \"email\": \"john@example.com\", \"mobile\": \"1234567890\"}"
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Doe\", \"email\": \"doe@example.com\", \"mobile\": \"0987654321\"}"
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Smith\", \"email\": \"smith@example.com\", \"mobile\": \"1122334455\"}"
    ```

2. **Add Expense** (Exact Split):
    ```bash
    curl -X POST http://127.0.0.1:5000/expense -H "Content-Type: application/json" -d "{\"description\": \"Shopping\", \"amount\": 4299, \"paid_by\": \"john\", \"splits\": {\"john\": 1500, \"doe\": 799, \"smith\": 2000}}"
    ```

3. **Get Balances**:
    ```bash
    curl http://127.0.0.1:5000/balances
    ```

4. **Generate Balance Sheet**:
    ```bash
    curl http://127.0.0.1:5000/balance-sheet
    ```

### 3. Percentage Split

#### Scenario:
You go to a party with 2 friends and one of your cousins. You owe 50%, Friend 1 owes 25%, and Friend 2 owes 25%.

#### Steps:

1. **Add Users**:
    ```bash
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Emily\", \"email\": \"emily@example.com\", \"mobile\": \"1234567890\"}"
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Frank\", \"email\": \"frank@example.com\", \"mobile\": \"0987654321\"}"
    curl -X POST http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Grace\", \"email\": \"grace@example.com\", \"mobile\": \"1122334455\"}"
    ```

2. **Add Expense** (Percentage Split):
    Assuming the total amount is 400.
    ```bash
    curl -X POST http://127.0.0.1:5000/expense -H "Content-Type: application/json" -d "{\"description\": \"Party\", \"amount\": 400, \"paid_by\": \"emily\", \"splits\": {\"emily\": 200, \"frank\": 100, \"grace\": 100}}"
    ```

3. **Get Balances**:
    ```bash
    curl http://127.0.0.1:5000/balances
    ```

4. **Generate Balance Sheet**:
    ```bash
    curl http://127.0.0.1:5000/balance-sheet
    ```

5. **Download Balance Sheet**:
    ```bash
    curl http://127.0.0.1:5000/download-balance-sheet -o balance_sheet.csv
    ```

## Why Choose Python?

Python was chosen for this project due to its many advantages over other programming languages, such as Java:

1. **Ease of Use and Readability**: Python's syntax is clean and easy to read, making it ideal for rapid development and prototyping.
2. **Rapid Development**: Python allows for faster development cycles due to its simplicity and extensive libraries.
3. **Strong Community Support**: Python has a large and active community, which means there are plenty of resources, libraries, and frameworks available.
4. **Versatility**: Python is highly versatile and can be used for a wide range of applications, from web development to data analysis and machine learning.
5. **Flask Framework**: Flask is a lightweight and flexible web framework that makes it easy to create web applications quickly. It is well-suited for small to medium-sized projects like this expense sharing application.

By using Python and Flask, we were able to build a robust and feature-rich application efficiently and effectively.

## Conclusion

This application provides a comprehensive solution for managing and sharing daily expenses among multiple users. With the ability to add users, manage expenses, split costs using various methods, and download the balance sheet as a CSV file, it meets all the specified requirements. The choice of Python and Flask ensures that the application is easy to develop, maintain, and extend in the future.

We hope this project demonstrates our technical skills and attention to detail. If you have any questions or need further assistance, please feel free to contact us.
