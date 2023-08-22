from pathlib import Path
from git_orchestrator import GitOrchestrator



class FileHandler:
    def __init__(self, file_path: Path):
        if file_path.is_file():
            self.file_path = file_path
            self.file_name = self.file_path.name
            self.file_extension = self.file_path.suffix[1:]
            self.file_str = GitOrchestrator.retrieve_file(self.file_path) 
        else:
            raise Exception("FileHandler_Path_Error: The given path is not a file")

    def __str__(self):
        string = f"\nfile_path: {self.file_path}\nfile_name: {self.file_name}\nfile_extension: {self.file_extension}\nfile_str:\n\n{self.file_str}\n\n"
        return string
