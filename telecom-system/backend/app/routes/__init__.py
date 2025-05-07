from .company import company_bp
from flask import Blueprint, request, jsonify
from app.models import Company
from app import db

company_bp = Blueprint('company', __name__)

@company_bp.route('/', methods=['POST'])
def add_company():
    data = request.get_json()
    name = data.get('name')
    address = data.get('address')
    phone = data.get('phone')

    if not name:
        return jsonify({'error': 'Company name is required'}), 400

    new_company = Company(name=name, address=address, phone=phone)
    db.session.add(new_company)
    db.session.commit()

    return jsonify({'message': 'Company added', 'id': new_company.id}), 201

@company_bp.route('/', methods=['GET'])
def list_companies():
    companies = Company.query.all()
    result = [{
        'id': c.id,
        'name': c.name,
        'address': c.address,
        'phone': c.phone
    } for c in companies]
    return jsonify(result)
