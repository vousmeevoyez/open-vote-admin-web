"""
    Define all required form here
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import *

## login and registration
class LoginForm(FlaskForm):
    """ form for login """
    username = TextField('Username')
    password = PasswordField('Password')

class CreateAccountForm(FlaskForm):
    """ form for create user """
    username = TextField('Username')
    identity_id = TextField('Identity ID')
    name = TextField('Name')
    email = TextField('Email')
    msisdn = TextField('Phone Number')
    password = PasswordField('Password')
    role = SelectField('Role', choices=[("PARTICIPANT", "PARTICIPANT"),
                                        ("ADMIN", "ADMIN"),
                                        ("COMMITEE", "COMMITEE"),
                                       ])

class CreateCandidateForm(FlaskForm):
    """ form for create election form """
    name = TextField('Candidate Name')
    description = TextField('Candidate Description')
    order_no = TextField('Candidate No')
    #file = FileField('File', validators=[
    #    FileRequired(),
    #    FileAllowed(['pdf'], 'PDF only!')
    #])
    
class CreateElectionForm(FlaskForm):
    """ form for create election form """
    name = TextField('Election Name')
    description = TextField('Election Description')