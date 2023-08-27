from pathlib import Path
from file_scrapper import FileScrapper
from git_manager import GitManager
from git_file_checker import GitFileChecker
from pygit2 import GIT_OBJ_COMMIT
from modified_files_manager import ModifiedFilesManager
from file_handler import FileHandler
from documentation_manager import DocumentationManager
if __name__ == "__main__":
    # algo = Path("./src/doc_ignore.py")

    # # Abre el repositorio
    # repo = GitManager.project_repo()
    # repo_path = "."  # Asumiendo que estás en la raíz del repositorio, sino, cambia la ruta.

    # # Obtiene el commit más reciente
    # head = repo.head
    # commit = repo[head.target]

    # # Función recursiva para recorrer el tree y obtener las rutas de los archivos
    # def get_file_paths(tree, parent_path=Path('.')):
    #     paths = []
    #     for entry in tree:
    #         full_path: Path = parent_path / entry.name
    #         if full_path.exists():
    #             if full_path.is_file():
    #                 paths.append(full_path)
    #             elif not entry.type == GIT_OBJ_COMMIT:
    #                 if full_path.is_dir():
    #                     print(entry.type)
    #                     paths.extend(get_file_paths(repo[entry.oid], full_path))
    #         else: 
    #             raise Exception('something went wrong')
    #     return paths

    # # Obtiene todas las rutas
    # file_paths = get_file_paths(commit.tree)

    # # Imprime las rutas
    # for path in file_paths:
    #     print(path)
    # GitManager.select_front_commit()
    # file_scrapper = FileScrapper()
    # a = file_scrapper._start_current_file_paths()
    # GitFileChecker.update_changed_files()
    # file_scrapper.scrape_specified(GitFileChecker.modified)
    # print(file_scrapper._code_scrapper._show())
    DocumentationManager.run_diagnosis()
    DocumentationManager.show_results()
    pass
