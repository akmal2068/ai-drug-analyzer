const API = "http://127.0.0.1:5000";

function register() {
    fetch(`${API}/register`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                username: document.getElementById("username").value,
                password: document.getElementById("password").value
            })
        })
        .then(res => res.json())
        .then(data => alert(data.message || data.error));
}

function login() {
    fetch(`${API}/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                username: document.getElementById("username").value,
                password: document.getElementById("password").value
            })
        })
        .then(res => res.json())
        .then(data => {
            if (data.access_token) {
                localStorage.setItem("token", data.access_token);
                window.location.href = "dashboard.html";
            } else {
                alert("Login failed");
            }
        });
}

let lastDrugData = null;

function searchDrug() {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Loading...";

    const token = localStorage.getItem("token");

    fetch(`${API}/drug-info`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                ...(token && { "Authorization": `Bearer ${token}` })
            },
            body: JSON.stringify({
                drug: document.getElementById("drugName").value,
                mode: document.getElementById("mode").value
            })
        })
        .then(res => res.json())
        .then(data => {
            lastDrugData = data; // store safely

            resultDiv.innerHTML = `
            <b>Drug:</b> ${data.drug}<br>
            <b>Uses:</b> ${data.uses}<br>
            <b>Dosage:</b> ${data.dosage}<br>
            <b>Side Effects:</b> ${data.side_effects}<br>
            <b>Warnings:</b> ${data.warnings}<br>
            <b>Interactions:</b> ${data.interactions}<br>
            <button type="button" onclick="downloadReport()">Download Report</button>
        `;
        })
        .catch(error => {
            console.error(error);
            resultDiv.innerHTML = "Error fetching data.";
        });
}

function loadHistory() {
    const token = localStorage.getItem("token");

    fetch(`${API}/history`, {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        })
        .then(res => res.json())
        .then(data => {
            let html = "";
            data.forEach(item => {
                html += `<p>${item.drug} (${item.mode}) - ${item.time}</p>`;
            });
            document.getElementById("history").innerHTML = html;
        });
}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

function downloadReport() {
    if (!lastDrugData) return;

    let text = `
Drug Report
-----------
Drug: ${lastDrugData.drug}
Uses: ${lastDrugData.uses}
Dosage: ${lastDrugData.dosage}
Side Effects: ${lastDrugData.side_effects}
Warnings: ${lastDrugData.warnings}
Interactions: ${lastDrugData.interactions}
    `;

    let blob = new Blob([text], { type: "text/plain" });
    let a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = `${lastDrugData.drug}_report.txt`;
    a.click();
}