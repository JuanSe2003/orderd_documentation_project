# Problema: 
Se quiere documentar las clases de tal fomr aque se pueda llevar registro metodo a
metodo, como los metodos son funciones en python, y en general en otro AST tambien son funciones queremos llevar el registro y la relación de cada metodo con su clase padre, o incluso de clases anidadas con su clase padre, y que se pueda recuperar el padre y con la informacion que tiene el hijo poder recuperar toda la informacion del padre.

# Solucion: 
Llevar registro del nodo padre con la información necesaria para encontrar su hash. 
                self.file_path,
                self.file_name,
                self.file_extension,
                self.code_snippet_type,
                self.code_snippet_identifier,

crear una clase que sea parent_node_type, parent_identifier, node, y a partir de esta trabajar, como snippet extract o dependencies, mejorar la logica recursiva de tree stitter util _descendants_with_type
los primeros 3, los debe compartir con el hijo, el hijo solo deberia guardar el tipo de snippet del padre y su identificador. Con esa misma informaccion se puede acceder al mismo hash del objeto ya guardado y de esa forma acceder a su implementacion.
Pensar en que hay que modificar el hashing porque puede cambiar de tiempo de ejecucion a tiempo de ejecucion.