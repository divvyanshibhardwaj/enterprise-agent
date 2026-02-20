from agent.skill_registry import load_skills

def route(context):

    skills = load_skills()

    for skill_name, skill_data in skills.items():

        caps = skill_data.get("capabilities", {})

        if (
            caps.get("task_type") == context["task_type"]
            and context["language"] in caps.get("language", [])
            and caps.get("input_type") == context["input_type"]
        ):
            return skill_name

    return "unknown"