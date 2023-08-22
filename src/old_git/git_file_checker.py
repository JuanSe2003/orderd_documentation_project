from git_manager import GitManager
from pygit2 import Diff, Commit, GIT_DELTA_ADDED, GIT_DELTA_MODIFIED, GIT_DELTA_DELETED
from typing import Dict
from singleton_meta import SingletonMeta
from pathlib import Path


class GitFileChecker(metaclass=SingletonMeta):
    _git_manager: GitManager

    def __init__(self):
        self._git_manager = GitManager()

    def check_file_changes(
        self, tail_commit: Commit = None, head_commit: Commit = None
    ) -> Dict[str, Path]:
        tail_commit = (
            self._git_manager._selected_commit if tail_commit == None else tail_commit
        )
        head_commit = (
            self._git_manager._head_commit if head_commit == None else head_commit
        )
        files_diff = self._get_diff(tail_commit, head_commit)
        return self._extract_changes(files_diff)

    def _get_diff(self, tail_commit: Commit, head_commit: Commit) -> Diff:
        return self._git_manager._project_repo.diff(tail_commit, head_commit)

    def _extract_changes(self, files_diff: Diff) -> Dict[str, Path]:
        files_changes = {"added": [], "modified": [], "deleted": []}
        for patch in files_diff:
            if patch.delta.status == GIT_DELTA_ADDED:
                files_changes["added"].append(Path(patch.delta.new_file.path))
            elif patch.delta.status == GIT_DELTA_MODIFIED:
                files_changes["modified"].append(Path(patch.delta.new_file.path))
            elif patch.delta.status == GIT_DELTA_DELETED:
                files_changes["deleted"].append(Path(patch.delta.old_file.path))
        return files_changes
