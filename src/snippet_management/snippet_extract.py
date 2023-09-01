from tree_sitter_logic.tree_sitter_util import get_identifier, get_implementation
from dataclasses import dataclass
from tree_sitter import Node


@dataclass()
class SnippetExtract:
    snippet_type: str
    snippet_identifier: str
    snippet_implementation: str

    def __init__(self, node: Node, file_str: str):
        self.snippet_type = node.type
        self.snippet_identifier = get_identifier(node, file_str)
        self.snippet_implementation = get_implementation(node, file_str)
