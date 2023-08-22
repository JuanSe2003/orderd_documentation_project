from file_scrapper import FileScrapper
from git_orchestrator import GitOrchestrator

class ModifiedFilesManager:
    _git_orchestrator: GitOrchestrator
    _file_scrapper_tail: FileScrapper
    _file_scrapper_head: FileScrapper

    #implementar lo que dice el to-do