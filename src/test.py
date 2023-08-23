from git_orchestrator import GitOrchestrator
from pathlib import Path
from file_scrapper import FileScrapper
from git_manager import GitManager
from pygit2 import GIT_OBJ_COMMIT
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
    file_scrapper = FileScrapper()
    file_scrapper._start_current_file_paths()
    print(file_scrapper._current_file_paths)
    pass
