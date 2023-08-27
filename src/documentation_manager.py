from snippet_storage import SnippetStorage
from typing import List, ClassVar
from pathlib import Path
from modified_files_manager import ModifiedFilesManager
from added_files_manager import AddedFilesManager
from git_file_checker import GitFileChecker
from singleton_meta import SingletonMeta

#GitFileChecker. Solo se ha de usar su update aqui
class DocumentationManager(metaclass=SingletonMeta):
    instance: ClassVar
    _snippets_to_doc: SnippetStorage
    _snippets_to_delete: SnippetStorage
    _files_to_delete: List[Path]

    def __init__(self):
        self._snippets_to_doc = SnippetStorage()
        self._snippets_to_delete = SnippetStorage()
        self._files_to_delete = None

    def _update_snippets_to_doc(self):
        AddedFilesManager.check_added_files()
        added_file_snippets_dict = AddedFilesManager.get_snippets_to_doc().storage
        self._snippets_to_doc.update_storage(added_file_snippets_dict)
        ModifiedFilesManager.check_modified_files()
        modified_file_snippets_dict = ModifiedFilesManager.get_snippets_to_doc().storage
        self._snippets_to_doc.update_storage(modified_file_snippets_dict)

    def _update_snippets_to_delete(self):
        ModifiedFilesManager.check_modified_files()
        deleted_file_snippets_dict = (
            ModifiedFilesManager.get_snippets_to_delete().storage
        )
        self._snippets_to_delete.update_storage(deleted_file_snippets_dict)

    def _update_files_to_delete(self):
        self._files_to_delete = GitFileChecker.deleted

    @staticmethod
    def run_diagnosis():
        GitFileChecker.update_changed_files()
        DocumentationManager.instance._update_snippets_to_doc()
        DocumentationManager.instance._update_snippets_to_delete()
        DocumentationManager.instance._update_files_to_delete()

    @staticmethod
    def get_snippets_to_doc() -> SnippetStorage:
        return DocumentationManager.instance._snippets_to_doc
    
    @staticmethod
    def get_snippets_to_delete() -> SnippetStorage:
        return DocumentationManager.instance._snippets_to_delete
    
    @staticmethod 
    def show_results():
        print('-------------------------------------------------------------\n')
        print('\t\tSNIPPETS TO DOCUMENTATE\n')
        print('-------------------------------------------------------------\n')
        DocumentationManager.get_snippets_to_doc().show_storage()
        print('\n\n\n\n')
        print('-------------------------------------------------------------\n')
        print('\t\tSNIPPETS TO DELETE\n')
        print('-------------------------------------------------------------\n')
        DocumentationManager.get_snippets_to_delete().show_storage()
        print('-------------------------------------------------------------\n')
        print('\n\n\nEND')

documentation_manager = DocumentationManager()