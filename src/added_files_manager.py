from file_scrapper import FileScrapper
from snippet_storage import SnippetStorage
from git_file_checker import GitFileChecker
from typing import ClassVar, Dict
from singleton_meta import SingletonMeta
from git_manager import GitManager
class AddedFilesManager(metaclass=SingletonMeta):
    instance: ClassVar
    _added_file_scrapper : FileScrapper
    _snippets_to_doc: SnippetStorage

    def __init__(self):
        self._added_file_scrapper = FileScrapper()
        self._snippets_to_doc = SnippetStorage()

    def _start_added_file_scrapper(self):
        if GitFileChecker.added:
            GitManager.select_front_commit()
            self._added_file_scrapper.scrape_specified(GitFileChecker.added)

    def _update_snippets_to_doc(self):
        self._start_added_file_scrapper()
        snippets_to_doc_dict = self._added_file_scrapper.storage_dict
        self._snippets_to_doc.update_storage(snippets_to_doc_dict)

    @staticmethod
    def get_snippets_to_doc() -> SnippetStorage:
        return AddedFilesManager.instance._snippets_to_doc
    
    @staticmethod
    def check_added_files():
        AddedFilesManager.instance._update_snippets_to_doc()

AddedFilesManager = AddedFilesManager()