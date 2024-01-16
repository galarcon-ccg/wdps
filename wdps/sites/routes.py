from flask import Blueprint

wdps = Blueprint('wdps', __name__, url_prefix='/wdps')

@wdps.route("/")
def index():
    return "welcome RegulonDB-wdps"