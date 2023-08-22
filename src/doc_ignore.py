""" 
Doc Ignore va a leer un archivo de texto y va agregar cada linea a un 
conjunto, despues el file scrapper, antes de leer un archivo, 
va a corroborar que el nombre del archivo no este, o su extension,
y tambien carpetas
"""
from dataclasses import dataclass
from pathlib import Path
from singleton_meta import SingletonMeta
class DocIgnore(metaclass=SingletonMeta):
    """ 
    Este archivo siempre debe estar en una carpeta en el primer nivel del proyecto
    ya que se deberia buscar la carpeta raiz del proyecto en si 
    """
    def __init__(self, root_path: Path = None):
        project_root = root_path if root_path != None else DocIgnore._get_path()
        doc_ignore = project_root / '.docignore'
        if doc_ignore.exists():
            read_doc = doc_ignore.read_text()
            doc_lines = read_doc.splitlines()
            doc_set = set(doc_lines)
            clean_doc_set = {line.strip() for line in doc_set}
            self.ignore = clean_doc_set
        else:
            raise Exception('DocIgnore_.docignore_not_found: .docignore is not at the root dir')

    def __contains__(self, sys_object: str):
        return sys_object in self.ignore

    @staticmethod
    def _get_path():
        return Path.cwd()