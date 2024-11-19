from flask import Flask, request, render_template

app = Flask(__name__)

# Dummy database
accounts = {
    "123": 1000.50,
    "456": 250.00,
    "789": 300.75
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/balance', methods=['POST'])
def balance():
    account_id = request.form.get('account_id')
    balance = accounts.get(account_id, None)
    if balance is not None:
        return render_template('balance.html', account_id=account_id, balance=balance)
    else:
        return render_template('balance.html', error="Account ID not found!")

if __name__ == "__main__":
    app.run(debug=True)
