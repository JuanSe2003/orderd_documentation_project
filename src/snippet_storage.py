from dataclasses import dataclass, field
from singleton_meta import SingletonMeta
from code_snippet import CodeSnippet
from typing import Dict, Union

#deja de ser singleton ya que se necesita comparar almacenamientos. 
@dataclass
class SnippetStorage:
    _storage: Dict[int, CodeSnippet] = field(default_factory=dict)

    def __contains__(self, code_snippet: CodeSnippet):
        return isinstance(self.get_code_snippet(code_snippet), CodeSnippet)

    def get_code_snippet(self, code_snippet: CodeSnippet) -> Union[CodeSnippet, None]:
        hashed_snippet = hash(code_snippet)
        if hashed_snippet in self._storage:
            return self._storage.get(hashed_snippet)
        else:
            return None

    def add_code_snippet(self, code_snippet: CodeSnippet) -> bool:
        if code_snippet in self:
            return False
        hashed_snippet = hash(code_snippet)
        self._storage.update({hashed_snippet: code_snippet})
        return True

    def update_code_snippet(self, code_snippet: CodeSnippet) -> bool:
        # only changes the implementation
        if code_snippet not in self:
            return False
        hashed_snippet = hash(code_snippet)
        self._storage.update({hashed_snippet: code_snippet})
        return True

    def delete_code_snippet(self, code_snippet: CodeSnippet) -> bool:
        if code_snippet not in self:
            return False
        hashed_snippet = hash(code_snippet)
        self._storage.pop(hashed_snippet)
        return True
    
    def _show_storage(self):
        for key, value in (self._storage).items():
            print(f'{key}: {value}')
