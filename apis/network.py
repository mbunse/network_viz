from flask_restplus import Resource, Namespace, fields
import pandas as pd


api = Namespace('network', description='Netzwerk abfragen')

edge = api.model('Edge', {
        "start": fields.Integer(),
        "target": fields.Integer()
})

node = api.model("Node", {
    "id": fields.Integer(),
    "name": fields.String()
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
            pd.unique(df[["start", "target"]].values.ravel())
        ).reset_index(name="name").rename(columns={"index": "id"})

        # Create a map to map node names to ids
        map_nodes = nodes.set_index("name").iloc[:, 0]

        # Map nodes to ids in list of edges
        df.replace({"start": map_nodes}, inplace=True)
        df.replace({"target": map_nodes}, inplace=True)

        return {"network": {
            "nodes": nodes.to_dict("records"),
            "edges": df.to_dict(orient="records")}
        }