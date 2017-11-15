from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from flask import Flask
from app.mod_search.api import mod_search

app = Flask("indexer-search")
app.register_blueprint(mod_search)


xray_recorder.configure(service="indexer-search")
XRayMiddleware(app, xray_recorder)

