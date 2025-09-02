from models import Session, Client

def get_session():
    return Session()

def validate_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def get_client_summary():
    session = Session()
    clients = session.query(Client).all()
    
    client_data = []
    for client in clients:
        client_dict = {
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'hourly_rate': client.hourly_rate,
            'project_count': len(client.projects)
        }
        client_data.append(client_dict)
    
    session.close()
    return client_data