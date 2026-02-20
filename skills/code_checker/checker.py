import json

def check_file(file_path):
    violations = []

    with open("skills/code_checker/rules.json") as f:
        rules = json.load(f)

    with open(file_path) as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines, start=1):
        for rule in rules:
            if rule["pattern"] in line:
                violations.append({
                    "rule_id": rule["id"],
                    "message": rule["description"],
                    "severity": rule["severity"],
                    "line": line_number,
                    "code": line.strip()
                })

    return {
        "file": file_path,
        "total_violations": len(violations),
        "violations": violations
    }