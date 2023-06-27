from models.companies import Company
from app import db

def create_new_company(data):
    new_company = Company(name=data['name'], 
                          visibility=data['visibility'])
    db.session.add(new_company)
    db.session.commit()

def get_companies():
    companies = Company.query.all()
    result = []
    for company in companies:
        company_data = {
            'id': company.id,
            'name': company.name,
            'visibility': company.visibility,
            'grade': float(company.grade)   
        }
        result.append(company_data)
    return result

def get_specific_company(company_id):
    company = Company.query.get(company_id)
    if company:
        company_data = {
            'id': company.id,
            'name': company.name,
            'visibility': company.visibility,
            'grade': float(company.grade)
        }
        return company_data
    else:
        return None

def search_company_by_name(name):
    company = Company.query.filter_by(name=name).first()
    if company:
        company_data = {
            'id': company.id,
            'name': company.name,
            'visibility': company.visibility,
            'grade': float(company.grade)
        }
        return company_data
    else:
        return None

def update_company(company_id, data):
    company = Company.query.get(company_id)
    if company:
        company.name = data.get('name', company.name)
        company.visibility = data.get('visibility', company.visibility)
        db.session.commit()
        return True
    else:
        return False

def delete_company(company_id):
    company = Company.query.get(company_id)
    if company:
        db.session.delete(company)
        db.session.commit()
        return True
    else:
        return False
