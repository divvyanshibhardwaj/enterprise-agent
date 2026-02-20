import sys
from agent.core import handle_request

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python main.py <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    task = "check my code"

    handle_request(task, input_file)