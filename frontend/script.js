function calculate() {
  const mid1 = document.getElementById("mid1").value;
  const mid2 = document.getElementById("mid2").value;
  const assign1 = document.getElementById("assign1").value;
  const assign2 = document.getElementById("assign2").value;
  const quiz1 = document.getElementById("quiz1").value;
  const quiz2 = document.getElementById("quiz2").value;
  const attendance = document.getElementById("attendance").value;

  // ✅ validation (VERY IMPORTANT)
  if (
    !mid1 || !mid2 || !assign1 || !assign2 ||
    !quiz1 || !quiz2 || !attendance
  ) {
    document.getElementById("result").innerText =
      "Please fill all fields";
    return;
  }

  const data = {
    mid1: Number(mid1),
    mid2: Number(mid2),
    assign1: Number(assign1),
    assign2: Number(assign2),
    quiz1: Number(quiz1),
    quiz2: Number(quiz2),
    attendance: Number(attendance)
  };

  console.log("SENDING DATA:", data); // DEBUG

  fetch("https://student-performance-api-hgij.onrender.com/calculate-internal", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
    .then(res => res.json())
    .then(result => {
      console.log("API RESPONSE:", result);
      document.getElementById("result").innerText =
        "Internal Marks (out of 30): " + result.internal_marks_out_of_30;
    })
    .catch(() => {
      document.getElementById("result").innerText =
        "Error connecting to API";
    });
}
