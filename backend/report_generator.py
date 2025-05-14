import json
from datetime import datetime

def generate_json_report(data, filename="report.json"):
    report = {
        "timestamp": datetime.now().isoformat(),
        "summary": data
    }
    with open(filename, "w") as f:
        json.dump(report, f, indent=2)
    return filename