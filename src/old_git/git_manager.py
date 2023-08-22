from pathlib import Path
from singleton_meta import SingletonMeta
from pygit2 import Repository, Commit, Tree

#integrar todas las utilidades como atributos del git manager o una clase orquestadora que inicialice el GitManager y todas las utilidades
#cambiar a git repo manager
class GitManager(metaclass=SingletonMeta):
    instance = None
    _project_repo: Repository
    _head_commit: Commit
    _selected_commit: Commit # default = HEAD^
    _commit_tree: Tree

    def __init__(self, repo_path: Path = Path.cwd(), selected_commit_hash: str = None):
        self._project_repo = Repository(repo_path)
        self._head_commit = self._project_repo.head.peel(Commit)
        if selected_commit_hash != None:
            self._selected_commit = self._project_repo[selected_commit_hash]
        elif self._head_commit.parents:
            self._selected_commit = self._head_commit.parents[0]
        else:
            raise Exception(
                "GitRetrieval_Specify_Commit: Not commit was specified, and not exists HEAD's parents commit to use."
            )
        self._commit_tree = self._selected_commit.tree

    def update_selected_commit(self, selected_commit_hash: str):
        self._selected_commit = self._project_repo[selected_commit_hash]
        self._commit_tree = self._selected_commit.tree