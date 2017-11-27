#from app.common.indexer_provider import ElasticProvider
from flask import Blueprint, abort
import json, time


mod_search = Blueprint("mod_search", __name__, url_prefix="/search")
#elastic_provider = ElasticProvider("indexer-imovel", "imovel")


@mod_search.route("/<description>", methods=["GET"])
def search(description):
    # Pesquisas realizadas no Elasticsearch são feitas utilizando query DSL no formato JSON
    query = {"query": {"prefix": {"description": description}}}

    # retorna os dados provenientes do Elasticsearch
    #return elastic_provider.search(query)

    return json.dumps({"requested":"ok"})


@mod_search.route("/", methods=["GET"])
def get_status():
    return "its working - search"


@mod_search.route("/get_aborted", methods=["GET"])
def get_status_aborted():
    return abort(400)