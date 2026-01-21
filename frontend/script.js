function calculate() {

    const data = {
        mid1: Number(document.getElementById("mid1").value),
        mid2: Number(document.getElementById("mid2").value),
        assign1: Number(document.getElementById("assign1").value),
        assign2: Number(document.getElementById("assign2").value),
        quiz1: Number(document.getElementById("quiz1").value),
        quiz2: Number(document.getElementById("quiz2").value),
        attendance: Number(document.getElementById("attendance").value)
    };

    fetch("http://127.0.0.1:8000/calculate-internal", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById("result").innerText =
            "Internal Marks (out of 30): " + result.internal_marks_out_of_30;
    })
    .catch(error => {
        document.getElementById("result").innerText =
            "Error connecting to API";
    });
}