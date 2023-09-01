from documentation_orchestrator.documentation_manager import DocumentationManager
from git_tools.git_file_paths import GitFilePaths
from pathlib import Path
if __name__ == "__main__":
    # DocumentationManager.start_documentation()
    # DocumentationManager.show_results()
    print(GitFilePaths.get_all_valid_paths())
