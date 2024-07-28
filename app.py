from flask import Flask, request, jsonify, send_file
from expense_app import ExpenseSharingApp
import csv
import io

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

expense_app = ExpenseSharingApp()

@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    mobile = data.get('mobile')
    message = expense_app.add_user(name, email, mobile)
    return jsonify({"message": message})

@app.route('/user/<name>', methods=['GET'])
def get_user(name):
    user_details = expense_app.get_user_details(name)
    return jsonify(user_details)

@app.route('/expense', methods=['POST'])
def add_expense():
    data = request.json
    description = data.get('description')
    amount = data.get('amount')
    paid_by = data.get('paid_by')
    splits = data.get('splits')
    message = expense_app.add_expense(description, amount, paid_by, splits)
    return jsonify({"message": message})

@app.route('/balances', methods=['GET'])
def get_balances():
    balances = expense_app.calculate_balances()
    return jsonify(balances)

@app.route('/balance-sheet', methods=['GET'])
def generate_balance_sheet():
    balance_sheet = expense_app.generate_balance_sheet()
    return jsonify(balance_sheet)

@app.route('/download-balance-sheet', methods=['GET'])
def download_balance_sheet():
    balance_sheet = expense_app.generate_balance_sheet()
    
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write header
    writer.writerow(['User', 'Balance'])
    
    # Write balance data
    for user, balance in balance_sheet.items():
        writer.writerow([user, balance])
    
    output.seek(0)
    
    return send_file(io.BytesIO(output.getvalue().encode()), 
                     mimetype='text/csv', 
                     as_attachment=True, 
                     download_name='balance_sheet.csv')

if __name__ == '__main__':
    app.run(debug=True)
