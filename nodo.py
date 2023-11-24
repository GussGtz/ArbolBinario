class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario: 
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        def _insertar_recursivo(nodo, nuevo_dato):
            if nuevo_dato < nodo.dato:
                if nodo.izquierda is None:
                    nodo.izquierda = NodoArbol(nuevo_dato)
                else:
                    _insertar_recursivo(nodo.izquierda, nuevo_dato)
            else:
                if nodo.derecha is None:
                    nodo.derecha = NodoArbol(nuevo_dato)
                else:
                    _insertar_recursivo(nodo.derecha, nuevo_dato)

        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            _insertar_recursivo(self.raiz, dato)

    def buscar(self, dato):
        def _buscar_recursivo(nodo, dato):
            if nodo is None or nodo.dato == dato:
                return nodo
            if dato < nodo.dato:
                return _buscar_recursivo(nodo.izquierda, dato)
            return _buscar_recursivo(nodo.derecha, dato)

        return _buscar_recursivo(self.raiz, dato)

    def eliminar(self, dato):
        def _eliminar_recursivo(nodo, dato):
            if nodo is None:
                return None
            if dato < nodo.dato:
                nodo.izquierda = _eliminar_recursivo(nodo.izquierda, dato)
            elif dato > nodo.dato:
                nodo.derecha = _eliminar_recursivo(nodo.derecha, dato)
            else:
                if nodo.izquierda is None:
                    return nodo.derecha
                elif nodo.derecha is None:
                    return nodo.izquierda
                min_larger_node = self._encontrar_minimo(nodo.derecha)
                nodo.dato = min_larger_node.dato
                nodo.derecha = _eliminar_recursivo(nodo.derecha, min_larger_node.dato)
            return nodo

        self.raiz = _eliminar_recursivo(self.raiz, dato)

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def recorrer_inOrden(self):
        resultado = []
        def _inOrden(nodo):
            if nodo:
                _inOrden(nodo.izquierda)
                resultado.append(nodo.dato)
                _inOrden(nodo.derecha)
        _inOrden(self.raiz)
        return resultado

    def recorrer_preOrden(self):
        resultado = []
        def _preOrden(nodo):
            if nodo:
                resultado.append(nodo.dato)
                _preOrden(nodo.izquierda)
                _preOrden(nodo.derecha)
        _preOrden(self.raiz)
        return resultado

    def recorrer_postOrden(self):
        resultado = []
        def _postOrden(nodo):
            if nodo:
                _postOrden(nodo.izquierda)
                _postOrden(nodo.derecha)
                resultado.append(nodo.dato)
        _postOrden(self.raiz)
        return resultado

    def mostrar_arbol(self, nodo=None, nivel=0):
        if self.raiz is None:
            print("El árbol está vacío.")
            return
        if nodo is None:
            nodo = self.raiz
        if nodo is not None:
            if nodo.derecha is not None:
                self.mostrar_arbol(nodo.derecha, nivel + 1)
            print("    " * nivel + str(nodo.dato))
            if nodo.izquierda is not None:
                self.mostrar_arbol(nodo.izquierda, nivel + 1)

    def interactuar(self):
        while True:
            print("\nOperaciones disponibles:")
            print("1. Insertar")
            print("2. Eliminar")
            print("3. Buscar")
            print("4. Mostrar árbol")
            print("5. Salir")

            eleccion = input("Elige una opción (1-5): ")

            if eleccion == "1":
                dato = int(input("Ingresa el número a insertar: "))
                self.insertar(dato)
                print("Número insertado.")
            elif eleccion == "2":
                dato = int(input("Ingresa el número a eliminar: "))
                self.eliminar(dato)
                print("Número eliminado.")
            elif eleccion == "3":
                dato = int(input("Ingresa el número a buscar: "))
                nodo = self.buscar(dato)
                if nodo:
                    print(f"Elemento {dato} encontrado.")
                else:
                    print(f"Elemento {dato} no encontrado.")
            elif eleccion == "4":
                print("\nÁrbol Binario:")
                self.mostrar_arbol()
            elif eleccion == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")
arbol = ArbolBinario()
arbol.interactuar()
