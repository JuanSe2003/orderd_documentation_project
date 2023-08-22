from dataclasses import dataclass, field, asdict
import json
from pathlib import Path
from snippet_extract import SnippetExtract
from file_handler import FileHandler


@dataclass()
class CodeSnippet:
    file_path: Path
    file_name: str
    file_extension: str
    code_snippet_type: str
    code_snippet_identifier: str
    code_snippet_implementation: str = field(hash=False)

    def __init__(self, file_handler: FileHandler, snippet_extract: SnippetExtract):
        self.file_path = file_handler.file_path
        self.file_name = file_handler.file_name
        self.file_extension = file_handler.file_extension
        self.code_snippet_type = snippet_extract.snippet_type
        self.code_snippet_identifier = snippet_extract.snippet_identifier
        self.code_snippet_implementation = snippet_extract.snippet_implementation

    def __hash__(self):
        return hash(
            (
                self.file_path,
                self.file_name,
                self.file_extension,
                self.code_snippet_type,
                self.code_snippet_identifier,
            )
        )

    def __str__(self):
        string = f"\n\nfile_path: {self.file_path}\nfile_name: {self.file_name}\nfile_extension: {self.file_extension}\nsnippet_type: {self.code_snippet_type}\nsnippet_identifier: {self.code_snippet_identifier}\nsnippet_implementation:\n\n{self.code_snippet_implementation}\n"
        return string

    def json(self) -> str:
        return json.dumps(asdict(self))

    @staticmethod
    def to_code_snippet(snippet_json: str):
        return CodeSnippet(**(json.loads(snippet_json)))
