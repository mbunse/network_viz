from flask_restplus import Resource, Namespace, fields
import pandas as pd


api = Namespace('network', description='Netzwerk abfragen')

edge = api.model('Edge', {
        "from": fields.Integer(),
        "to": fields.Integer()
})

node = api.model("Node", {
    "id": fields.Integer(),
    "label": fields.String()
})

nodes_and_edges = api.model("Nodes_And_Edges", {
    "nodes": fields.List(fields.Nested(node)),
    "edges": fields.List(fields.Nested(edge))
})
network = api.model("Network", {
    "network": fields.Nested(nodes_and_edges)
})


@api.route("/")
class Network(Resource):
    @api.marshal_with(network)
    def get(self):
        df = pd.read_csv("data/network.csv")
        # Extract unique nodes
        nodes = pd.Series(
            pd.unique(df[["from", "to"]].values.ravel())
        ).reset_index(name="label").rename(columns={"index": "id"})

        # Create a map to map node names to ids
        map_nodes = nodes.set_index("label").iloc[:, 0]

        # Map nodes to ids in list of edges
        df.replace({"from": map_nodes}, inplace=True)
        df.replace({"to": map_nodes}, inplace=True)

        return {"network": {
            "nodes": nodes.to_dict("records"),
            "edges": df.to_dict(orient="records")}
        }