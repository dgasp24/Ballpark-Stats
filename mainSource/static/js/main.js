const checkGraph = document.getElementById("graph");
const checkTable = document.getElementById("table");
const table = document.getElementById("divTable");
const graph = document.getElementById("graph-container")
const scatterBtn = document.getElementById("scatter")
const barBtn = document.getElementById("bar")
const statsDiv = document.getElementById("statsDiv")

const stat1 = document.createElement("select")
const stat2 = document.createElement("select")
stat1.name = "statChoice"
stat2.name = "statChoice2"
stat1.classList.add('animate__animated', 'animate__fadeInUp', 'animate__faster');
stat2.classList.add('animate__animated', 'animate__fadeInUp', 'animate__faster');


//CREATING SELECT OPTIONS FOR SECOND STAT
const optionsData = [
        {text: "Stat", value: 'none'},
    {text: "Batting Average", value: 1},
    {text: "OPS", value: 2},
    {text: "Homeruns", value: 3},
    {text: "SLG", value: 4}
];

optionsData.forEach(data => {
    const option = document.createElement('option');
    option.text = data.text;
    option.value = data.value;
    stat1.appendChild(option)

    const option2 = document.createElement('option');
    option2.text = data.text;
    option2.value = data.value;
    stat2.appendChild(option2);
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
    if (statsDiv.contains(stat2)) {
        statsDiv.removeChild(stat2);
    }
    statsDiv.append(stat1);
    stat1.options[0].text = "Stat";
    stat1.classList.add('animate__animated', 'animate__fadeInUp');
});

scatterBtn.addEventListener("click", () => {
    scatterBtn.classList.add("active");
    barBtn.classList.remove("active");
    if (statsDiv.contains(stat1)) {
        statsDiv.removeChild(stat1);
    }
    stat1.options[0].text = "Stat 1 (X-Axis)";
    stat2.options[0].text = "Stat 2 (Y-Axis)";
    statsDiv.append(stat1);
    statsDiv.append(stat2);
});

