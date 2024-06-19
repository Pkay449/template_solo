import os
import shutil


def create_project():
    project_name = input("Enter the project name: ")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.dirname(script_dir)
    new_project_path = os.path.join(base_path, project_name)
    os.makedirs(new_project_path, exist_ok=True)

    # Directories including nested structures
    directories = [
        "src/utils",
        "src/models",
        "src/services",
        "tests",
        "docs",
        "data",
        "scripts",
        "notebooks",
        ".github",
        "config",
        "examples",
    ]
    files = {
        "README.md": "",
        "LICENSE": "",
        ".gitignore": "",
        "requirements.txt": "",
        "setup.py": "",
        "src/utils/helper.py": "# Helper functions",
        "src/models/user.py": "# User model",
        "src/services/database.py": "# Database services",
        "src/services/authentication.py": "# Authentication services",
    }

    # Create directories
    for directory in directories:
        os.makedirs(os.path.join(new_project_path, directory), exist_ok=True)

    # Create files
    for file_path, content in files.items():
        full_path = os.path.join(new_project_path, file_path)
        with open(full_path, "w") as file:
            file.write(content)

    # Copy documentation files
    source_docs_path = os.path.join(base_path, "docs")
    target_docs_path = os.path.join(new_project_path, "docs")
    docs_files = [
        "project_structure.md",
        "steps.md",
        "visual_sketch.md",
    ]  # Make sure visual_sketch.md is correct
    for doc in docs_files:
        shutil.copy(os.path.join(source_docs_path, doc), target_docs_path)

    # Copy the directory_tree.py script
    shutil.copy(
        os.path.join(script_dir, "directory_tree.py"),
        os.path.join(new_project_path, "scripts"),
    )

    print(f"Project {project_name} created successfully!")


if __name__ == "__main__":
    create_project()
