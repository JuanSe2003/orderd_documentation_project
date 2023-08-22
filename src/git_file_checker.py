from git_manager import GitManager
from pygit2 import Diff, Commit, GIT_DELTA_ADDED, GIT_DELTA_MODIFIED, GIT_DELTA_DELETED
from typing import Dict
from pathlib import Path
from no_instanciable_meta import NoInstanciable

# Todo manejo de git se debe hacer a través de gitManager
class GitFileChecker(metaclass=NoInstanciable):
    @staticmethod
    def check_file_changes() -> Dict[str, Path]:
        tail_commit = GitManager.selected_commit()
        head_commit = GitManager.head_commit()
        files_diff = GitFileChecker._get_diff(tail_commit, head_commit)
        return GitFileChecker._extract_changes(files_diff)

    @staticmethod
    def _get_diff(tail_commit: Commit, head_commit: Commit) -> Diff:
        return GitManager.project_repo().diff(tail_commit, head_commit)

    @staticmethod
    def _extract_changes(files_diff: Diff) -> Dict[str, Path]:
        files_changes = {"added": [], "modified": [], "deleted": []}
        for patch in files_diff:
            if patch.delta.status == GIT_DELTA_ADDED:
                files_changes["added"].append(Path(patch.delta.new_file.path))
            elif patch.delta.status == GIT_DELTA_MODIFIED:
                files_changes["modified"].append(Path(patch.delta.new_file.path))
            elif patch.delta.status == GIT_DELTA_DELETED:
                files_changes["deleted"].append(Path(patch.delta.old_file.path))
        return files_changes
