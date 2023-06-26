from flask import request, Response
from services.companyService import *
from app import app
import json


@app.route('/company', methods=['POST'])
def create_company():
    data = request.get_json()
    create_new_company(data)
    return Response(json.dumps({'message': 'Company created successfully!'}), status=200, mimetype="application/json")


@app.route('/companies', methods=['GET'])
def get_all_companies():
    companies = get_companies()
    return Response(json.dumps(companies), status=200, mimetype="application/json")


@app.route('/company/<int:company_id>', methods=['GET'])
def get_company_by_id(company_id):
    company = get_specific_company(company_id)
    if company:
        return Response(json.dumps(company), status=200, mimetype="application/json")
    else:
        return Response(json.dumps({'error': 'Company not found'}), status=404, mimetype="application/json")


@app.route('/company/search/<string:name>', methods=['GET'])
def get_company_by_name(name):
    company = search_company_by_name(name)
    if company:
        return Response(json.dumps(company), status=200, mimetype="application/json")
    else:
        return Response(json.dumps({'error': 'Company not found'}), status=404, mimetype="application/json")


@app.route('/company/<int:company_id>', methods=['PUT'])
def update_company_info(company_id):
    company = get_specific_company(company_id)
    if company:
        data = request.get_json()
        update_company(company_id, data)
        return Response(json.dumps({'message': 'Company information updated successfully'}), status=200,
                        mimetype="application/json")
    else:
        return Response(json.dumps({'error': 'Company not found'}), status=404, mimetype="application/json")


@app.route('/company/<int:company_id>', methods=['DELETE'])
def delete_company_by_id(company_id):
    company = get_specific_company(company_id)
    if company:
        delete_company(company_id)
        return Response(json.dumps({'message': 'Company information updated successfully'}), status=200,
                        mimetype="application/json")
    else:
        return Response(json.dumps({'error': 'Company not found'}), status=404, mimetype="application/json")
