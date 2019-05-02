from flask import Blueprint

blueprint = Blueprint(
    'administrator',
    __name__,
    url_prefix='/admin',
    template_folder='templates',
    static_folder='static'
)
