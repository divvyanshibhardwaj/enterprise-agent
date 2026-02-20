import json
import sys
from skills.code_checker.checker import check_file

def run(input_data):

    result = check_file(input_data)

    print(json.dumps(result, indent=2))

    # ⭐ FAIL BUILD IF VIOLATIONS EXIST
    if result["total_violations"] > 0:
        print("\n❌ Code violations found!")
        sys.exit(1)