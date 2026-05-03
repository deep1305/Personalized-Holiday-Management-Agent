import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "Personalized_Holiday_Management"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/settings.py",
    f"{project_name}/agents/__init__.py",
    f"{project_name}/agents/planner.py",
    f"{project_name}/agents/researcher.py",
    f"{project_name}/teams/__init__.py",
    f"{project_name}/teams/holiday_team.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py",
    f"{project_name}/tests/__init__.py",
    f"{project_name}/tests/test_agents.py",
    "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
