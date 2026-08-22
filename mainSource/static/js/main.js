const checkGraph = document.getElementById("graph");
const checkTable = document.getElementById("table");
const table = document.getElementById("divTable");
const graph = document.getElementById("graph-container")
const scatterBtn = document.getElementById("scatter")
const barBtn = document.getElementById("bar")
const statsDiv = document.getElementById("statsDiv")


const stat1 = document.getElementById("statChoice")


const stat2 = document.createElement("select")
stat2.name = "statChoice2"


const optionsData = [
        {text: "Stat 2 (Y-Axis)", value: 'none'},
    {text: "Batting Average", value: 1},
    {text: "OPS", value: 2},
    {text: "Homeruns", value: 3},
    {text: "SLG", value: 4}
];

optionsData.forEach(data => {
    const option = document.createElement('option');
    option.text = data.text;
    option.value = data.value;
    stat2.appendChild(option)
})


checkGraph.addEventListener("click", () =>{
    graph.classList.toggle(("hidden"));
})

checkTable.addEventListener("click", () =>{
    table.classList.toggle("hidden");
})

barBtn.addEventListener("click", () => {
    barBtn.classList.add("active");
    scatterBtn.classList.remove("active");
    console.log("bar")
    stat1.options[0].text = "Stat";
    statsDiv.removeChild(stat2)
});

scatterBtn.addEventListener("click", () => {
    scatterBtn.classList.add("active");
    barBtn.classList.remove("active");
    console.log("scatter")
    stat1.options[0].text = "Stat 1 (X-Axis)";
    statsDiv.append(stat2)
});

