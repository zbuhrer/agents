import os
import json

with open('project-structure.json', 'r') as f:
    project_structure = json.load(f)

def create_project_structure(structure, path=""):
    for key, value in structure.items():
        if isinstance(value, dict) and value.get("type") == "directory":
            os.makedirs(f"{path}/{key}", exist_ok=True)
            create_project_structure(value["children"], f"{path}/{key}")
        elif value.get("type") == "file":
            open(f"{path}/{key}", "a").close()

create_project_structure(project_structure)
