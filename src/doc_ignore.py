""" 
Doc Ignore va a leer un archivo de texto y va agregar cada linea a un 
conjunto, despues el file scrapper, antes de leer un archivo, 
va a corroborar que el nombre del archivo no este, o su extension,
y tambien carpetas
"""
from pathlib import Path
from singleton_meta import SingletonMeta
from typing import ClassVar
from git_retrieaver import GitRetrieaver
from git_manager import GitManager
class DocIgnore(metaclass=SingletonMeta):
    """ 
    Este archivo siempre debe estar en una carpeta en el primer nivel del proyecto
    ya que se deberia buscar la carpeta raiz del proyecto en si 
    """
    instance: ClassVar
    def __init__(self, root_path: Path = None):
        project_root = root_path if root_path != None else Path('.')
        doc_ignore_path = project_root / '.docignore'
        if doc_ignore_path.exists():
            GitManager.select_front_commit()
            read_doc = GitRetrieaver.retrieve_file(doc_ignore_path)
            doc_lines = read_doc.splitlines()
            doc_set = set(doc_lines)
            clean_doc_set = {line.strip() for line in doc_set}
            self.ignore = clean_doc_set
        else:
            raise Exception('DocIgnore_.docignore_not_found: .docignore is not at the root dir')

    def __contains__(self, sys_object: str):
        return sys_object in self.ignore
