#!/usr/bin/env python3
print("Testing all application components...")

# Test database
try:
    from models import init_db
    init_db()
    print("✅ Database initialization successful")
except Exception as e:
    print(f"❌ Database error: {e}")

# Test CRUD operations
try:
    from crud import get_all_clients, get_all_projects, get_business_summary
    clients = get_all_clients()
    projects = get_all_projects()
    summary = get_business_summary()
    print("✅ CRUD operations successful")
except Exception as e:
    print(f"❌ CRUD error: {e}")

# Test CLI functionality
try:
    import click
    print("✅ Click import successful")
except Exception as e:
    print(f"❌ Click error: {e}")

print("All tests completed!")
