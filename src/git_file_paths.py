from git_manager import GitManager
from pathlib import Path
from pygit2 import Tree, GIT_OBJ_COMMIT
from typing import List
from doc_ignore import DocIgnore


# falta implementar el acceso a repositorios, pensar en monorepos raros
class GitFilePaths:
    doc_ignore = DocIgnore()

    @staticmethod
    def _valid_file(sys_path: Path) -> bool:
        return not (
            (sys_path.name in GitFilePaths.doc_ignore)
            or (sys_path.suffix in GitFilePaths.doc_ignore)
            or (sys_path.name == ".docignore")
            or (sys_path.name == ".git")
        )

    @staticmethod
    def get_all_paths(
        git_tree: Tree = GitManager.selected_commit_tree(),
        parent_path: Path = Path("."),
    ) -> List[Path]:
        paths: List[Path] = []
        for entry in git_tree:
            full_path: Path = parent_path / entry.name
            conditions = (
                not full_path.exists()
                or entry.type == GIT_OBJ_COMMIT
                or not GitFilePaths._valid_file(full_path)
            )
            if conditions:
                continue
            if full_path.is_file():
                paths.append(full_path)
            elif full_path.is_dir():
                dir_paths: List[Path] = GitFilePaths.get_all_paths(
                    GitManager.project_repo()[entry.oid], full_path
                )
                paths.extend(dir_paths)
        return paths
