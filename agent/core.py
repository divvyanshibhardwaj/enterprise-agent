from agent.router import route
from agent.context import build_context
from engine.executor import execute

def handle_request(task, input_data):

    context = build_context(task, input_data)

    skill = route(context)

    print(f"[Agent] Selected skill: {skill}")

    execute(skill, input_data)