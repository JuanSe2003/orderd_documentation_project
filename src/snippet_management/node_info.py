from dataclasses import dataclass
from tree_sitter import Node


@dataclass()
class NodeInfo:
    node: Node
    parent_type: str
    parent_identifier: str

    def __init__(self, root: Node):
        self.node = root
        self.parent_type = "program"
        self.parent_identifier = "program"

    def __init__(self, child_node: Node, parent_node: "NodeInfo", file_str: str):
        if parent_node.parent_type == "program":
            self.node = child_node
            self.parent_type = "root node"
            self.parent_identifier = "root node"
        else:
            self.node = child_node
            self.parent_type = parent_node.node.type
            self.parent_identifier = NodeInfo._get_identifier(
                parent_node.node, file_str
            )

    @property
    def children(self):
        return self.node.children
    
    @staticmethod
    def _get_identifier(node: Node, file_str: str) -> str:
        for child in node.children:
            if child.type == "identifier":
                return file_str[child.start_byte : child.end_byte]
        return None
