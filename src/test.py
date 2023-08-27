from pathlib import Path
from file_scrapper import FileScrapper
from git_manager import GitManager
from git_file_checker import GitFileChecker
from pygit2 import GIT_OBJ_COMMIT
from modified_files_manager import ModifiedFilesManager
from file_handler import FileHandler
from documentation_manager import DocumentationManager
from git_file_paths import GitFilePaths
if __name__ == "__main__":

    DocumentationManager.run_diagnosis()
    DocumentationManager.show_results()
    pass
