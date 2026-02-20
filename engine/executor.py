import importlib

def execute(skill_name, input_data):

    try:
        module_path = f"skills.{skill_name}.runner"

        skill_module = importlib.import_module(module_path)

        skill_module.run(input_data)

    except Exception as e:
        print(f"[Executor] Failed to execute skill: {e}")