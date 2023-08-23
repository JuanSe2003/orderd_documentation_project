from pathlib import Path
from singleton_meta import SingletonMeta
from pygit2 import Repository, Commit, Tree
from typing import ClassVar


class GitManager(metaclass=SingletonMeta):
    instance: ClassVar = None
    project_repo: Repository
    head_commit: Commit
    selected_commit: Commit  # default = HEAD^
    commit_tree: Tree

    def __init__(self, repo_path: Path = Path.cwd()):
        self.project_repo = Repository(repo_path)
        self.head_commit = self.project_repo.head.peel(Commit)
        if self.head_commit.parents[0]:
            self.selected_commit = self.head_commit.parents[0]
        else:
            raise Exception('GitManager_Error: get_head_parent_commit(), No head parent commit.')
        self.commit_tree = self.selected_commit.tree

    def _update_selected_commit(self, selected_commit_hash: str):
        self.selected_commit = self.project_repo[selected_commit_hash]
        self.commit_tree = self.selected_commit.tree

    @staticmethod
    def update_selected_commit(selected_commit_hash: str):
        GitManager.instance._update_selected_commit(selected_commit_hash)

    @staticmethod
    def project_repo() -> Repository:
        return GitManager.instance.project_repo

    @staticmethod
    def head_commit() -> Commit:
        return GitManager.instance.head_commit

    @staticmethod
    def selected_commit() -> Commit:
        return GitManager.instance.selected_commit

    @staticmethod
    def commit_tree() -> Tree:
        return GitManager.instance.commit_tree
    
    @staticmethod 
    def get_head_parent_commit() -> Commit:
        if GitManager.head_commit().parents[0]:
            return GitManager.head_commit().parents[0]
        else:
            raise Exception('GitManager_Error: get_head_parent_commit(), No head parent commit.')


GitManager()
