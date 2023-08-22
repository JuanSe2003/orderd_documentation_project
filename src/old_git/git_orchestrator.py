from git_manager import GitManager
from git_retrieval import GitRetrieval
from git_file_checker import GitFileChecker
from pathlib import Path
from typing import Dict
from singleton_meta import SingletonMeta
#posibilidad de implementar una clase para file_changes
class GitOrchestrator(metaclass=SingletonMeta):
    _git_manager: GitManager
    _git_retrieval: GitRetrieval
    _git_file_checker: GitFileChecker
    _files_changes: Dict[str, Path]

    def __init__(self):
        self._git_manager = GitManager()
        self._git_retrieval = GitRetrieval()
        self._git_file_checker = GitFileChecker()
        self._files_changes = self._git_file_checker.check_file_changes()

    def retrieve_file(self, file_path: Path, retrieval_commit_hash: str = None) -> str:
        self._git_retrieval.retrieve_file(file_path, retrieval_commit_hash)

    def update_selected_commit(self, selected_commit_hash: str):
        self._git_manager.update_selected_commit(selected_commit_hash)