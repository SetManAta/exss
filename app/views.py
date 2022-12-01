from flask import render_template, request, redirect, url_for,flash
from .models import Employee, User
from app import db
from .forms import EmployeeForm, UserForm
from flask_login import login_user, logout_user, login_required


def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@login_required
def employee_create():
    form = EmployeeForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            employees = Employee()
            form.populate_obj(employees)
            db.session.add(employees)
            db.session.commit()
            flash('сохранена GOOD')
            return redirect(url_for('index'))
    return render_template('employee_create.html', form=form)


def employee_detail(id):
    employees = Employee.query.get(id)
    return render_template('employee_detail.html', employees=employees)

@login_required
def employee_delete(id):
    employees = Employee.query.get(id)
    if request.method == 'POST':
        db.session.delete(employees)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('employee_delete.html', employees=employees)

@login_required
def employee_update(id):
    employees = Employee.query.get(id)
    form = EmployeeForm(request.form, obj=employees)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(employees)
            db.session.add(employees)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('employee_update.html', form=form)


# user functions

def register():
    form = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)
            db.session.add(user)
            db.session.commit()
            flash(f'Ползователь {user.username} save!','success')
            return redirect(url_for('index'))
    return render_template('register.html', form=form)


def login():
    form = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # user = User()
            # form.populate_obj(user)
            user = User.query.filter_by(username=request.form.get('username')).first()
            if user and user.check_password(request.form.get('password')):
                login_user(user)
                flash('Успешно авторизован!', 'primary')
                return redirect(url_for('index'))
            else:
                flash('не правильно введен логин или пароль','danger')
    return render_template('login.html', form=form)


def logout():
    logout_user()
    return redirect(url_for('index'))
