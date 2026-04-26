function getBestTime() {
    let item = document.getElementById("product").value;

    fetch(`http://127.0.0.1:5000/best-time?item=${item}`)
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            "Best hour: " + data.best_hour;
    });
}

function getTop() {
    fetch(`http://127.0.0.1:5000/top-products`)
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            JSON.stringify(data);
    });
}