import json
import csv

def export_to_json(data, filename="report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def export_to_csv(data, filename="report.csv"):
    keys = data.keys()
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(keys)
        writer.writerow([data[k] for k in keys])