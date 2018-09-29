
const myRequest = new Request("/api/network", 
    {
        method: 'GET',
        datatype: "json",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          }
    });
fetch(myRequest).then(response => response.json())
    .then(json => {

        var container = document.getElementById('chart-area');

        var edges_raw = json["network"]["edges"]
        for (edge of edges_raw) {
            edge["arrows"]="to"
        }
        var edges = new vis.DataSet(edges_raw);
        var nodes = new vis.DataSet(json["network"]["nodes"]);

        var data = {
            nodes: nodes,
            edges: edges
        };
        var options = {};
        var network = new vis.Network(container, data, options);
        
    });



