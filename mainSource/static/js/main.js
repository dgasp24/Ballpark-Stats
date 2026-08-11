const checkGraph = document.getElementById("graph");
const checkTable = document.getElementById("table");
const table = document.getElementById("divTable");
const graph = document.getElementById("graph-container")

checkGraph.addEventListener("click", () =>{
    graph.classList.toggle(("hidden"));
})

checkTable.addEventListener("click", () =>{
    table.classList.toggle("hidden");
})