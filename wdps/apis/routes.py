from flask import Blueprint, request
from web_services import WS_connect
from .ht.dataset.datasets import DatasetsSearch

api = Blueprint('api', __name__, url_prefix='/wdps/api')

@api.route("/")
def index():
    return "welcome RegulonDB-WDPS-APIS"

## DTT routes

@api.route("/dtt")
def index_dtt():
    return "welcome DTT serve"

#HT routes

@api.route("/ht")
def index_ht():
    return "welcome HT API"

# /wdps/api/ht/<file_format>
@api.route('/ht/<file_format>', methods=['GET', 'POST'])
def index_ht_datasets_by_format(file_format):
    file_format = file_format.lower()
    if request.method == 'POST':
        data_json = request.get_json()
        print(data_json)
        ws = WS_connect()
        if ws.is_connected():
            dataset_search = DatasetsSearch(data_json['advancedSearch'], False, ws.get_gql_service())
            dataset_search.get_data(file_format)
            return dataset_search.response
        else:
            return {"error": "ws connect error"}
    return {"error": "api no method support"}