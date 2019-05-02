"""
    Authentication Routes
"""
from flask import jsonify, render_template, redirect, request, url_for
from flask_login import logout_user

from app.authentication import blueprint
from app.forms import LoginForm, CreateAccountForm
from app.authentication.modules.auth_services import *

@blueprint.route('/login')
def login():
    """
        function to render login page
    """
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)

    return render_template(
        'login.html',
        login_form=login_form,
        create_account_form=create_account_form,
    )

@blueprint.route('/logout')
def logout():
    """
        function to logout user
    """
    logout_user()

    return redirect(url_for('index.index'))

@blueprint.route('/api/login', methods=['POST'])
def sign_in():
    """
        function to sign in user via AJAX
    """
    response = AuthServices().login(request.form)
    return response

@blueprint.route('/api/register', methods=['POST'])
def sign_up():
    """
        function to regist user via AJAX
    """
    response = AuthServices().register(request.form)
    return response
