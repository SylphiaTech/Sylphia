import { fetchData } from "./api";
import { renderDashboard } from "./components/dashboard";

async function startSylphiaApp() {
    const data = await fetchData();
    renderDashboard(data);
    setupExportButton(data);
}

function setupExportButton(data) {
    const btn = document.createElement("button");
    btn.textContent = "Export Report";
    btn.onclick = () => {
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: "application/json" });
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "sylphia_report.json";
        a.click();
    };
    document.body.appendChild(btn);
}

startSylphiaApp();