from flask import Blueprint, render_template, redirect, url_for

from forms import EmployeeForm
from models import Employee, db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    employees = Employee.query.all()
    title = "Employee Records"
    return render_template('index.html', employees=employees, title=title)


@main.route('/add', methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        employee = Employee(
            name=form.name.data,
            position=form.position.data,
            department=form.department.data,
            salary=form.salary.data,
            date_of_joining=form.date_of_joining.data,
            birthday=form.birthday.data,
            is_active=form.is_active.data
        )
        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('main.index'))
    title = "Add Employee"
    return render_template('employee_form.html', form=form, title=title)


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)
    form = EmployeeForm(obj=employee)
    if form.validate_on_submit():
        employee.name = form.name.data
        employee.position = form.position.data
        employee.department = form.department.data
        employee.salary = form.salary.data
        employee.date_of_joining = form.date_of_joining.data
        employee.birthday = form.birthday.data
        employee.is_active = form.is_active.data
        db.session.commit()
        return redirect(url_for('main.index'))
    title = "Edit Employee"
    return render_template('employee_form.html', form=form, employee=employee, title=title)


@main.route('/delete/<int:id>')
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('main.index'))
