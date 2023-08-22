from pathlib import Path
from pygit2 import Repository, Commit, Tree

#probelema si el repo no tiene suficientes commits
class GitManager:
    project_repo: Repository = Repository(Path.cwd())
    head_commit: Commit = Repository(Path.cwd()).head.peel(Commit)
    selected_commit: Commit = Repository(Path.cwd()).head.peel(Commit).parents[0]
    commit_tree: Tree = Repository(Path.cwd()).head.peel(Commit).parents[0].tree

    @staticmethod
    def _update_selected_commit(selected_commit_hash: str):
        GitManager.selected_commit = GitManager.project_repo[selected_commit_hash]
        GitManager.commit_tree = GitManager.selected_commit.tree
