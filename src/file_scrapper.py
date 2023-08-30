from code_scrapper import CodeScrapper
from file_handler import FileHandler
from doc_ignore import DocIgnore
from pathlib import Path
from typing import List, Dict
from git_manager import GitManager
from pygit2 import Tree, GIT_OBJ_COMMIT
from code_snippet import CodeSnippet
from git_file_checker import GitFileChecker

# dejar una sola función que sea que scrape specified y obtener todas las rutas de interes recorriendo el commit tree.
# añadir variable que me diga cuales archivos han sido documentados
class FileScrapper:
    _root_dir: Path
    _current_file: FileHandler
    _code_scrapper: CodeScrapper
    _ignore: DocIgnore

    def __init__(self, root_dir: Path = Path(".")):
        self._root_dir = root_dir
        self._ignore = DocIgnore(root_dir)
        self._code_scrapper = CodeScrapper()
        self._current_file = None

    def scrape_specified(self, specified_files: List[Path]) -> bool:
        for file_path in specified_files:
            if self._valid_file(file_path):
                print(f'{file_path}, valid', GitManager.selected_commit())
                self._start_scrape(file_path)
        return True

    @property
    def storage_dict(self) -> Dict[int, CodeSnippet]:
        return self._code_scrapper.storage_dict

    def _update_current_file(self, file_path: Path):
        self._current_file = FileHandler(file_path)

    def _start_scrape(self, file_path: Path):
        self._update_current_file(file_path)
        self._code_scrapper.change_file(self._current_file)
        self._code_scrapper.extract_snippets()

    def _valid_file(self, sys_path: Path) -> bool:
        divide_path = str(sys_path).split("\\")
        return not (
            (any(path_name in self._ignore for path_name in divide_path))
            or (sys_path.suffix in self._ignore)
            or (sys_path.name == ".docignore")
            or (sys_path.name == ".git")
            or (sys_path.name == "doc.log")
        )

