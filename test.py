from lib.models import Session, Client

def test_connection():
    try:
        session = Session()
        clients = session.query(Client).all()
        print(f"Found {len(clients)} clients")
        session.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if test_connection():
        print("Database connection successful!")
    else:
        print("Database connection failed!")