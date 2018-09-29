from flask_restplus import Resource, Namespace, fields
import pandas as pd


api = Namespace('network', description='Netzwerk abfragen')

edge = api.model('Edge', {
        "start": fields.String(),
        "target": fields.String()
})
network = api.model("Network", {
    "network": fields.List(
        fields.Nested(edge))
})

@api.route("/")
class Network(Resource):
    @api.marshal_with(network)
    def get(self):
        df = pd.read_csv("data/network.csv")
        return {"network": df.to_dict(orient="records")}