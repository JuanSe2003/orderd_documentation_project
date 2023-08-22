from pathlib import Path
from singleton_meta import SingletonMeta
from git_manager import GitManager
from pygit2 import Blob
#git_manager must be initialized before all git "utilities"
#change to GitRetrieaver
class GitRetrieval(metaclass=SingletonMeta):
    _git_manager: GitManager

    def __init__(self):
        self._git_manager = GitManager()

    def retrieve_file(self, file_path: Path, retrieval_commit_hash: str = None) -> str:
        if retrieval_commit_hash != None:
            self._git_manager.update_retrieval_commit(retrieval_commit_hash)
        file_git_id = (self._get_file_git_object(file_path)).oid
        file_git_blob = self._git_manager._project_repo[file_git_id]
        file_bytes_data = file_git_blob.data
        file_worked_data = file_bytes_data.decode("utf-8")
        return file_worked_data
    
    def _get_file_git_object(self, file_path: Path) -> Blob:
        path_way = str(file_path).split("\\")
        current_object = self._git_manager._commit_tree
        for path in path_way:
            current_object = current_object[path]
        return current_object