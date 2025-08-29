from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="freelancer-tracker",
    version="1.0.0",
    author="Maureen W Karimi",
    author_email="your-email@example.com",
    description="A CLI application for freelancers to track clients, projects, and time worked",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/freelancer-tracker",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "sqlalchemy==1.4.46",
        "click==8.1.3",
        "tabulate==0.9.0",
        "faker==18.9.0",
        "python-dotenv==1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "freelancer-tracker=cli:cli",  
        ],
    },
    include_package_data=True,
)