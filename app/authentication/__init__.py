from flask import Blueprint

blueprint = Blueprint(
    'authentication',
    __name__,
    url_prefix='/auth',
    template_folder='templates',
    static_folder='static'
)
