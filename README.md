Main Objective = Create a Goal Track Application using Python, Flask, SQL Alchemy, IaC on AWS with Terraform, Create a CI/CD pipeline with Jenkins

For this i'll need to create:
- A Database




Steve Notes:

 - Installing the app and dependencies
    
    INSTALL VIRTUAL ENVIRONMENT
    - pip -m venv venv (to create the virtual environment)

    START VIRTUAL ENVIRONMENT
    - If using WSL or Linux
        - source ./venv/bin/activate
    - If using Windows
        - ./venv/Scripts/Activate.ps1

    UPGRADE PIP
    - pip install -U pip

    INSTALL DEPENDENCIES IN EDITABLE MODE
    - pip install -e .

    CREATE LOCAL DB FOR TESTING
    - python3 create_database.py

    START APPLICATION (cli command now available)
    - goal_tracker