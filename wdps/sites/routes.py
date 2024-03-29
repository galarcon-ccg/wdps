import os
from flask import Blueprint, render_template, send_file, request
from .gene.src import gene_list

#wdps routes
wdps = Blueprint('wdps', __name__, url_prefix='/wdps', template_folder="./wdps/templates", static_folder="./wdps/static")

@wdps.route("/")
def index():
    return render_template('index.html')

@wdps.route("/<organism_id>")
def organism_page(organism_id):
    return render_template('/ecoli/index.html')

#Statics
@wdps.route('/static/<type>/<file_name>')
def static_file(type, file_name):
    ruta_script = __file__
    dir_absoluto = os.path.dirname(os.path.abspath(ruta_script))
    dir = dir_absoluto+'/wdps/static/'+type+'/'
    path = os.path.join(dir, file_name)
    print(path)
    if os.path.exists(path):
        return send_file(path, as_attachment=True, download_name=file_name)
    else:
        print("file ",file_name," no found in route ",path)
        return "file no found"

#gene routes

gene = Blueprint('gene',__name__,url_prefix='/wdps/gene', template_folder="./gene/templates", static_folder="./gene/static")

@gene.route("/",methods=["POST","GET"] )
def gene_index():
    organism_id = request.args.get("organism_id")
    if organism_id is None:
        return "Error organism id"
    return gene_list()