# use 'pip install -e .' to install the package in development mode

from setuptools import setup, find_packages

setup(
    name='goal_tracker',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'goal_tracker = goalt_app.run:main'
        ]
    },
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'sqlalchemy'
    ]
)