from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
from urllib.parse import quote_plus  # Needed to import quote_plus for URL encoding

app = Flask(__name__)

db_user = 'root'
db_password = quote_plus('Pari@18nov')
db_host = 'localhost'
db_port = '3306'
db_name = 'telecom_db'

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = (f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models

class Company(db.Model):
    company_id = db.Column(db.String(50), primary_key=True)
    location = db.Column(db.String(100), nullable=False)
    branch_name = db.Column(db.String(100), nullable=False)

class Plan(db.Model):
    plan_id = db.Column(db.String(50), primary_key=True)
    plan_name = db.Column(db.String(100), nullable=False)
    plan_details = db.Column(db.String(200), nullable=False)

class NetworkInfrastructure(db.Model):
    network_id = db.Column(db.String(50), primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)

class Customer(db.Model):
    customer_id = db.Column(db.String(50), primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)

class Employee(db.Model):
    employee_id = db.Column(db.String(50), primary_key=True)
    employee_name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

# Insert Company
@app.route('/insert-company', methods=['POST'])
def insert_company():
    if request.method == 'POST':
        company_id = request.form['company_id']
        location = request.form['location']
        branch_name = request.form['branch_name']
        
        new_company = Company(company_id=company_id, location=location, branch_name=branch_name)
        db.session.add(new_company)
        db.session.commit()
        return redirect(url_for('index'))

# Insert Plan
@app.route('/insert-plan', methods=['POST'])
def insert_plan():
    if request.method == 'POST':
        plan_id = request.form['plan_id']
        plan_name = request.form['plan_name']
        plan_details = request.form['plan_details']
        
        new_plan = Plan(plan_id=plan_id, plan_name=plan_name, plan_details=plan_details)
        db.session.add(new_plan)
        db.session.commit()
        return redirect(url_for('index'))

# Insert Network Infrastructure
@app.route('/insert-network-infrastructure', methods=['POST'])
def insert_network_infrastructure():
    if request.method == 'POST':
        network_id = request.form['network_id']
        type = request.form['type']
        location = request.form['location']
        
        new_network = NetworkInfrastructure(network_id=network_id, type=type, location=location)
        db.session.add(new_network)
        db.session.commit()
        return redirect(url_for('index'))

# Insert Customer
@app.route('/insert-customer', methods=['POST'])
def insert_customer():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        customer_name = request.form['customer_name']
        address = request.form['address']
        
        new_customer = Customer(customer_id=customer_id, customer_name=customer_name, address=address)
        db.session.add(new_customer)
        db.session.commit()
        return redirect(url_for('index'))

# Insert Employee
@app.route('/insert-employee', methods=['POST'])
def insert_employee():
    if request.method == 'POST':
        employee_id = request.form['employee_id']
        employee_name = request.form['employee_name']
        department = request.form['department']
        
        new_employee = Employee(employee_id=employee_id, employee_name=employee_name, department=department)
        db.session.add(new_employee)
        db.session.commit()
        return redirect(url_for('index'))

# Run the app on port 8000
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
