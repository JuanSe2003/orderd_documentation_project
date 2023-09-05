from tree_sitter import Node
from typing import List, Set


def _descendants_with_type(node: Node, node_type: str) -> List[Node]:
    nodes = list()
    if node.type == node_type:
        nodes.append(node)
    for child in node.children:
        nodes.extend(_descendants_with_type(child, node_type))
    return nodes


def global_node_types(root: Node, node_types: Set[str]) -> List[Node]:
    return [child for child in root.children if child.type in node_types]


def get_specified_nodes(root: Node, node_types: Set[str]) -> List[Node]:
    nodes = list()
    for node_type in node_types:
        nodes.extend(_descendants_with_type(root, node_type))
    return nodes


def get_identifier(node: Node, file_str: str) -> str:
    for child in node.children:
        if child.type == "identifier":
            return file_str[child.start_byte : child.end_byte]
    return None


def get_dependencies(root: Node) -> List[Node]:
    dependencies_types = {'import_from_statement', 'import_from_statement'}
    return global_node_types(root, dependencies_types)

def get_implementation(node: Node, file_str: str) -> str:
    return file_str[node.start_byte : node.end_byte]
