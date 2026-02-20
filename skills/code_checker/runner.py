import json
from skills.code_checker.checker import check_file

def run(input_data):
    print(f"[Skill] Checking file: {input_data}")

    result = check_file(input_data)

    print("\n=== JSON REPORT ===")
    print(json.dumps(result, indent=2))