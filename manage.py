"""
    Manage
    ___________________
    This is flask application entry
"""
import csv
import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db

app = create_app(os.getenv("ENVIRONMENT") or 'dev')
app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    """ function to start flask apps"""
    host = os.getenv("HOST") or '127.0.0.1'
    port = os.getenv("PORT") or '5000'
    app.run(host=host,port=port)

@manager.command
def test():
    """ function to run unittest"""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command
def init():
    """ create init function here """
    pass

def make_shell_context():
    """ create shell context here"""
    pass

manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == "__main__":
    manager.run()
