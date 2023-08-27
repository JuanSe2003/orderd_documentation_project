from git_manager import GitManager
from pygit2 import Diff, Commit, GIT_DELTA_ADDED, GIT_DELTA_MODIFIED, GIT_DELTA_DELETED
from typing import Dict
from pathlib import Path
from no_instanciable_meta import NoInstanciable
from typing import List
# Todo manejo de git se debe hacer a través de gitManager
class GitFileChecker(metaclass=NoInstanciable):
    added: List[Path] = []
    modified: List[Path] = []
    deleted: List[Path] = []
    files_diff: Diff
    @staticmethod
    def update_changed_files():
        tail_commit = GitManager.tail_commit()
        front_commit = GitManager.front_commit()
        GitFileChecker.files_diff = GitFileChecker._get_diff(tail_commit, front_commit)
        GitFileChecker._extract_changes()

    @staticmethod
    def _get_diff(tail_commit: Commit, head_commit: Commit) -> Diff:
        return GitManager.project_repo().diff(tail_commit, head_commit)

    @staticmethod
    def _extract_changes():
        for patch in GitFileChecker.files_diff:
            if patch.delta.status == GIT_DELTA_ADDED:
                GitFileChecker.added.append(Path(patch.delta.new_file.path))
            elif patch.delta.status == GIT_DELTA_MODIFIED:
                GitFileChecker.modified.append(Path(patch.delta.new_file.path))
            elif patch.delta.status == GIT_DELTA_DELETED:
                GitFileChecker.deleted.append(Path(patch.delta.old_file.path))

