from flask import Blueprint
from flask_restplus import Api

from .network import api as ns_api

import pandas as pd

blueprint = Blueprint('api', __name__, url_prefix="/api")

api = Api(blueprint,
          Title="Netwerk API",
          version=0.1,
          description="",
          doc="/doc"
)

api.add_namespace(ns_api)