from flask import Flask
from app.mod_search.api import mod_search

app = Flask("indexer-search")
app.register_blueprint(mod_search)
