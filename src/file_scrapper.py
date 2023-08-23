from code_scrapper import CodeScrapper
from file_handler import FileHandler
from doc_ignore import DocIgnore
from pathlib import Path
from typing import List
from git_manager import GitManager
from pygit2 import Tree, GIT_OBJ_COMMIT


# dejar una sola función que sea que scrape specified y obtener todas las rutas de interes recorriendo el commit tree.
# añadir variable que me diga cuales archivos han sido documentados
class FileScrapper:
    _root_dir: Path
    _current_file: FileHandler
    _code_scrapper: CodeScrapper
    _ignore: DocIgnore
    _current_file_paths: List[Path]

    def __init__(self, root_dir: Path = Path(".")):
        self._root_dir = root_dir
        self._ignore = DocIgnore(root_dir)
        self._code_scrapper = CodeScrapper()
        self._current_file = None
        self._current_file_paths = None

    def scrape_specified(self, specified_files: List[Path]) -> bool:
        for file_path in specified_files:
            self._start_scrape(file_path)
        return True

    def _update_current_file(self, file_path: Path):
        self._current_file = FileHandler(file_path)

    def _start_scrape(self, file_path: Path):
        self._update_current_file(file_path)
        self._code_scrapper.change_file(self._current_file)
        self._code_scrapper.extract_snippets()

    def _start_current_file_paths(self):
        self._current_file_paths = self._get_all_git_file_path()
    # falta implementar el acceso a repositorios, pensar en monorepos raros
    def _get_all_git_file_path(
        self, git_tree: Tree = GitManager.commit_tree(), parent_path: Path = Path(".")
    ) -> List[Path]:
        paths: List[Path] = []
        for entry in git_tree:
            full_path: Path = parent_path / entry.name
            conditions = (
                not full_path.exists()
                or entry.type == GIT_OBJ_COMMIT
                or not self._valid_file(full_path)
            )
            if conditions:
                continue
            if full_path.is_file():
                paths.append(full_path)
            elif full_path.is_dir():
                dir_paths: List[Path] = self._get_all_git_file_path(
                    GitManager.project_repo()[entry.oid], full_path
                )
                paths.extend(dir_paths)
        return paths

    def _valid_file(self, sys_path: Path) -> bool:
        return not (
            (sys_path.name in self._ignore)
            or (sys_path.suffix in self._ignore)
            or (sys_path.name == ".docignore")
            or (sys_path.name == ".git")
        )
