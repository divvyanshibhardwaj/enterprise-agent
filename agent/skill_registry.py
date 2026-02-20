import os
import json

SKILLS_PATH = "skills"

def load_skills():
    skills = {}

    for folder in os.listdir(SKILLS_PATH):
        skill_file = os.path.join(SKILLS_PATH, folder, "skill.json")

        if os.path.exists(skill_file):
            with open(skill_file) as f:
                data = json.load(f)
                skills[data["name"]] = data

    return skills