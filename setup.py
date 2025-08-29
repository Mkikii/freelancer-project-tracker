# setup.py
from setuptools import setup

setup(
    name="freelancer-tracker",
    version="1.0.0",
    py_modules=['cli', 'crud', 'models', 'seed', 'debug'],
    install_requires=[
        "sqlalchemy==1.4.46",
        "click==8.1.3",
        "tabulate==0.9.0",
        "faker==18.9.0",
        "python-dotenv==1.0.0",
    ],
    entry_points={
        'console_scripts': [
            'freelancer-tracker=cli:cli',
        ],
    },
)