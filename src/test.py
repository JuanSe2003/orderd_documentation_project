from pathlib import Path
from file_scrapper import FileScrapper
from git_manager import GitManager
from code_scrapper import CodeScrapper
from git_file_checker import GitFileChecker
from doc_ignore import DocIgnore
from pygit2 import GIT_OBJ_COMMIT
from modified_files_manager import ModifiedFilesManager
from file_handler import FileHandler
from documentation_manager import DocumentationManager
from git_file_paths import GitFilePaths
from doc_log import DocLog
if __name__ == "__main__":
    DocumentationManager.start_documentation()
    DocumentationManager.show_results()
    ModifiedFilesManager.get_snippets_to_doc()
    print(GitFileChecker.added, GitFileChecker.deleted, GitFileChecker.modified)
    print(GitFilePaths.get_all_valid_paths())
    pass
