from flask import request, Response, jsonify
from models.companies import Company
from app import app, db

@app.route('/company', methods=['POST'])
def create_company():
    data = request.get_json()
    new_company = Company(name=data['name'], 
                          visibility=data['visibility'])
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

@app.route('/company/<int:company_id>', methods=['GET'])
def get_company_by_id(company_id):
    company = Company.query.get(company_id)

    if company:
        company_data = {
            'id': company.id,
            'name': company.name,
            'visibility': company.visibility,
            'grade': company.grade
        }
        return jsonify(company_data)
    else:
        return jsonify({'error': 'Company not found'}), 404
    
@app.route('/company/search/<string:name>', methods=['GET'])
def get_user_by_name(name):
    company = Company.query.filter_by(name=name).first()

    if company:
        company_data = {
            'id': company.id,
            'name': company.name,
            'visibility': company.visibility,
            'grade': company.grade
        }
        return jsonify(company_data)
    else:
        return jsonify({'error': 'company not found'})


@app.route('/company/<int:company_id>', methods=['PUT'])
def update_company_info(company_id):
    company = Company.query.get(company_id)

    if company:
        data = request.get_json()
        company.name = data.get('name', company.name)
        company.visibility = data.get('visibility', company.visibility)

        db.session.commit()

        return jsonify({'message': 'Company information updated successfully'})
    else:
        return jsonify({'error': 'Company not found'}), 404

@app.route('/company/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    company = Company.query.get(company_id)

    if company:
        db.session.delete(company)
        db.session.commit()
        return jsonify({'message': 'Company deleted successfully'})
    else:
        return jsonify({'error': 'Company not found'}), 404
