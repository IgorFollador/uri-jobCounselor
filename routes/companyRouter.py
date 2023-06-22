from flask import request, Response, jsonify
from models.companies import Company
from api import app, db

@app.route('/company', methods=['POST'])
def create_company():
    data = request.get_json()
    new_company = Company(name=data['name'], 
                          visibility=data['visibility'], 
                          username=data['username'], 
                          password=data['password'])
    db.session.add(new_company)
    db.session.commit()
    return jsonify({'message': 'Company created successfully!'})

@app.route('/companies', methods=['GET'])
def get_all_companies():
    companies = Company.query.all()
    result = []
    for company in companies:
        company_data = {
            'id': company.id,
            'name': company.name,
            'visibility': company.visibility,
            'grade': company.grade   
        }
        result.append(company_data)
    return jsonify(result)