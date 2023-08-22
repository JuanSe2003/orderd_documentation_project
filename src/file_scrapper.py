from code_scrapper import CodeScrapper
from file_handler import FileHandler
from doc_ignore import DocIgnore
from pathlib import Path
from typing import List


# añadir variable que me diga cuales archivos han sido documentados
class FileScrapper:
    _root_dir: Path
    _current_file: FileHandler
    _code_scrapper: CodeScrapper
    _ignore: DocIgnore

    def __init__(self, root_dir: Path = Path.cwd()):
        self._root_dir = root_dir
        self._ignore = DocIgnore(root_dir)
        self._code_scrapper = CodeScrapper()
        self._current_file = None

    def travel_and_scrape(self, initial_dir: Path = None) -> bool:
        init_dir = initial_dir if initial_dir != None else self._root_dir
        for item in init_dir.iterdir():
            if item.is_file() and self._check_file(item):
                self._start_scrape(item)
            elif item.is_dir() and self._check_file(item):
                self.travel_and_scrape(item)
        return True

    def scrape_specified(self, specified_files: List[Path]) -> bool:
        for file_path in specified_files:
            self._start_scrape(file_path)
        return True

    def _update_current_file(self, file_path: Path, use_selected_commit: bool = False):
        self._current_file = FileHandler(file_path, use_selected_commit)

    def _start_scrape(self, file_path: Path):
        self._update_current_file(file_path)
        self._code_scrapper.change_file(self._current_file)
        self._code_scrapper.extract_snippets()

    def _check_file(self, sys_path: Path) -> bool:
        return not (
            (sys_path.name in self._ignore)
            or (sys_path.suffix in self._ignore)
            or (sys_path.name == ".docignore")
        )


path = Path.cwd()
print(path)

a = FileScrapper()
a.travel_and_scrape()
a._code_scrapper._show()
