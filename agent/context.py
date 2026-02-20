import os

def detect_language(file_name):

    ext = os.path.splitext(file_name)[1]

    mapping = {
        ".java": "java",
        ".py": "python",
        ".js": "javascript"
    }

    return mapping.get(ext, "unknown")


def build_context(task, input_data):

    language = detect_language(input_data)

    context = {
        "task_type": "code_analysis",
        "language": language,
        "input_type": "file"
    }

    print(f"[Context] Detected language: {language}")

    return context