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

document.querySelectorAll('.toggleBtn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.toggleBtn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        document.getElementById('chartType').value = btn.dataset.chart;
    });
});