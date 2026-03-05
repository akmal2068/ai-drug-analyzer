import os
from datetime import datetime

def save_report(drug_name, data):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = f"reports/{drug_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Drug: {drug_name}\n\n")
        f.write(f"Description:\n{data['description']}\n\n")
        f.write(f"Uses:\n{data['uses']}\n\n")
        f.write(f"Side Effects:\n{data['side_effects']}\n")

    return filename