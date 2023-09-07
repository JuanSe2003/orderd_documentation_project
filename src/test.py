from documentation_orchestrator.documentation_manager import DocumentationManager

from tree_sitter import Language, Parser


if __name__ == "__main__":
    # DocumentationManager.start_documentation()
    # DocumentationManager.show_results()
    # Cargar la gramática de Python
    PYTHON_LANGUAGE = Language('tree-sitter-python.so', 'python')
    parser = Parser()
    parser.set_language(PYTHON_LANGUAGE)

    # Código Python de ejemplo para parsear
    code = """
    def hello_world():
        print("Hello, World!")
    """

    # Parsear el código
    tree = parser.parse(bytes(code, "utf8"))

    # Obtener el nodo raíz y su tipo
    root_node = tree.root_node
    print(root_node.type)