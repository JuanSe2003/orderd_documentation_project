from git_manager import GitManager
from git_retrieaver import GitRetrieaver
from git_file_checker import GitFileChecker
from pathlib import Path
from typing import Dict
from no_instanciable_meta import NoInstanciable

# hacerlo un singleton solo para inicializar las cosas en orden 
class GitOrchestrator(metaclass=NoInstanciable):
    @staticmethod
    def retrieve_file(file_path: Path) -> str:
        GitManager()
        return GitRetrieaver.retrieve_file(file_path)

    @staticmethod
    def update_selected_commit(selected_commit_hash: str):
        GitManager()
        GitManager.update_selected_commit(selected_commit_hash)

    @staticmethod
    def get_files_changed() -> Dict[str, Path]:
        GitManager()
        return GitFileChecker.check_file_changes()
