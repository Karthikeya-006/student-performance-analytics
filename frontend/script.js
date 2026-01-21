function calculate() {

    const data = {
  mid1: Number(document.getElementById("mid1").value),
  mid2: Number(document.getElementById("mid2").value),

  assignment1: Number(document.getElementById("assign1").value),
  assignment2: Number(document.getElementById("assign2").value),

  quiz1: Number(document.getElementById("quiz1").value),
  quiz2: Number(document.getElementById("quiz2").value),

  attendance: Number(document.getElementById("attendance").value)
};

    fetch("https://student-performance-api-hgij.onrender.com/calculate-internal", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        console.log("API RESPONSE:",result)
        document.getElementById("result").innerText =
            "Internal Marks (out of 30): " + result.internal_marks_out_of_30;
    })
    .catch(error => {
        document.getElementById("result").innerText =
            "Error connecting to API";
    });
}
