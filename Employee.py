from datetime import date

from main_app import app
from models import db, Employee

# Dummy employee data
dummy_data = [
    {
        'name': 'Arun Sharma',
        'position': 'Software Engineer',
        'department': 'IT',
        'salary': 55000.00,
        'date_of_joining': date(2020, 6, 15),
        'birthday': date(1992, 3, 25),
        'is_active': True
    },
    {
        'name': 'Priya Verma',
        'position': 'HR Manager',
        'department': 'Human Resources',
        'salary': 60000.00,
        'date_of_joining': date(2019, 4, 10),
        'birthday': date(1985, 7, 18),
        'is_active': True
    },
    {
        'name': 'Rajesh Gupta',
        'position': 'Project Manager',
        'department': 'Operations',
        'salary': 80000.00,
        'date_of_joining': date(2018, 9, 1),
        'birthday': date(1983, 2, 20),
        'is_active': False
    },
    {
        'name': 'Nisha Reddy',
        'position': 'Marketing Executive',
        'department': 'Marketing',
        'salary': 45000.00,
        'date_of_joining': date(2021, 2, 5),
        'birthday': date(1990, 12, 10),
        'is_active': True
    },
    {
        'name': 'Suresh Kumar',
        'position': 'Sales Manager',
        'department': 'Sales',
        'salary': 75000.00,
        'date_of_joining': date(2017, 3, 19),
        'birthday': date(1987, 11, 5),
        'is_active': True
    },
    {
        'name': 'Meena Iyer',
        'position': 'Business Analyst',
        'department': 'Business Development',
        'salary': 65000.00,
        'date_of_joining': date(2020, 8, 23),
        'birthday': date(1993, 4, 17),
        'is_active': True
    },
    {
        'name': 'Anil Singh',
        'position': 'Software Developer',
        'department': 'IT',
        'salary': 50000.00,
        'date_of_joining': date(2022, 7, 5),
        'birthday': date(1995, 5, 9),
        'is_active': True
    },
    {
        'name': 'Geeta Patel',
        'position': 'Operations Executive',
        'department': 'Operations',
        'salary': 40000.00,
        'date_of_joining': date(2021, 11, 15),
        'birthday': date(1990, 10, 11),
        'is_active': False
    },
    {
        'name': 'Vikas Sharma',
        'position': 'Finance Manager',
        'department': 'Finance',
        'salary': 95000.00,
        'date_of_joining': date(2016, 1, 30),
        'birthday': date(1982, 6, 12),
        'is_active': True
    },
    {
        'name': 'Seema Malik',
        'position': 'Customer Support',
        'department': 'Customer Service',
        'salary': 35000.00,
        'date_of_joining': date(2023, 4, 2),
        'birthday': date(1995, 9, 6),
        'is_active': True
    }
]


# Insert dummy data into the database
def insert_dummy_data():
    for data in dummy_data:
        employee = Employee(
            name=data['name'],
            position=data['position'],
            department=data['department'],
            salary=data['salary'],
            date_of_joining=data['date_of_joining'],
            birthday=data['birthday'],
            is_active=data['is_active']
        )
        db.session.add(employee)

    # Commit the changes to the database
    db.session.commit()
    print("Dummy data inserted successfully!")


# Call the function to insert data
with app.app_context():
    insert_dummy_data()
