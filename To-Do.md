# Tarea: Extraer funciones que cambiaron desde el último commit
# Volver todos los git clases estaticas
1. Se debe usar pygit2 para obtener cuales archivos cambiaron de commit a commit, added, modified o deleted.
    - Los added se agregan directamente al conjunto de archivos a documentar directamente.
    - Los modified se agregan al conjunto de archivos a documentar comparando con el commit de interés. 
    - Los deleted se agregan al conjunto de archivos a eliminar de la documentación. 
2. Se debe manejar dos versiones paralelas del mismo archivo, commit A y commit B, el commit A es el commit más viejo, mientras que el commit B es el commit actual. 
3. Se debe  hacer extract_snippets de ambos archivos, tanto el archivo A como del archivo B. 
4. Se comparan los snippet_storage del scrapper A y el scrapper B snippet a snippet.
    1. Para obtener los snippets eliminados se hace A - B, añadiendolos al conjunto de eliminar . 
    2. Para obtener los snippets añadidos se hace B - A, añadiendolo al conjunto a documentar.
    3. Para obtener los snippets modificados se hace A intersección B y luego se comparan implementaciones como strings con dos posibles resultados.
        - La implementación es igual, por lo tanto no se agrega al conjunto a documentar.
        - La implementación es diferente, por lo tanto se agrega al conjunto a documentar. 

# Implementación. 

1. scrapper_A
2. scrapper_B
3. Cambiar la lógica de filehandler. 




# git retrieval 
1. debe recibir un file_path al cual se va a buscar una versión anterior. 
2. debe tener un atributo que contenga pygit.repo y tambien uno que guarde el commit history para poderlo recorrer. 
3. debe tener un metodo que retorne la implementación del commit especifico por parametro, el parametro por default es el commit antes del HEAD
4. se debe guardar el hash del commit del cual se va a recuperar el archivo y se debe guardar el str recuperado. 
´´´python
class GitRetrieval: 
    _file_path: Path 
    _project_repo: pygit.repo 
    _commit_history: List
    _retrieval_commit: CommitHash 

    def __init__(self, file_path: Path, _retrieval_commit: CommitHash = HEAD-1)
        self._file_path: Path 
´´´

# Hallar forma de documentar todas las dependencias de un archivo

# Cuidado con los subrepositorios, pensar en monorepo, polyrepo en cuanto al recorrido del los objetos de git

Por cada archivo se crea una carpeta y por cada nodo se crea un md 


# HEAD

# Falta aplicar la lógica que compara los dos snippet storage y verifica si la implementación es la misma o no.

# implementar el property para los atributos estaticos de la clase GitManager
# implementar un .log