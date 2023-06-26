from flask import request, jsonify
from services.companyService import *
from app import app

@app.route('/company', methods=['POST'])
def create_company():
    data = request.get_json()
    create_new_company(data)
    return jsonify({'message': 'Company created successfully!'})

@app.route('/companies', methods=['GET'])
def get_all_companies():
    companies = get_companies()
    return jsonify(companies)

@app.route('/company/<int:company_id>', methods=['GET'])
def get_company_by_id(company_id):
    company = get_specific_company(company_id)
    if company:
        return jsonify(company)
    else:
        return jsonify({'error': 'Company not found'}), 404

@app.route('/company/search/<string:name>', methods=['GET'])
def get_company_by_name(name):
    company = search_company_by_name(name)
    if company:
        return jsonify(company)
    else:
        return jsonify({'error': 'Company not found'})

@app.route('/company/<int:company_id>', methods=['PUT'])
def update_company_info(company_id):
    company = get_specific_company(company_id)
    if company:
        data = request.get_json()
        update_company(company_id, data)
        return jsonify({'message': 'Company information updated successfully'})
    else:
        return jsonify({'error': 'Company not found'}), 404

@app.route('/company/<int:company_id>', methods=['DELETE'])
def delete_company_by_id(company_id):
    company = get_specific_company(company_id)
    if company:
        delete_company(company_id)
        return jsonify({'message': 'Company deleted successfully'})
    else:
        return jsonify({'error': 'Company not found'}), 404
