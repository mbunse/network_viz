
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

        var edges = new vis.DataSet(json["network"]["edges"]);
        var nodes = new vis.DataSet(json["network"]["nodes"]);

        var data = {
            nodes: nodes,
            edges: edges
        };
        var options = {
            edges: {
                arrows: "to"
            },
            layout: {
                hierarchical: {
                    direction: "UD",
                    sortMethod: "directed"
                }
            }
        };
        var network = new vis.Network(container, data, options);
        
    });



