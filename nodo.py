import random

class Elemento:
    def __init__(self, valor):
        self.valor = valor
        self.hijo_izq = None
        self.hijo_der = None

class EstructuraArborea:
    def __init__(self, num_elementos=5, rango=(1, 100)):
        self.origen = None
        for _ in range(num_elementos):
            self.agregar(random.randint(*rango))

    def agregar(self, valor):
        def _agregar_aux(nodo, valor_nuevo):
            if valor_nuevo < nodo.valor:
                if nodo.hijo_izq is None:
                    nodo.hijo_izq = Elemento(valor_nuevo)
                else:
                    _agregar_aux(nodo.hijo_izq, valor_nuevo)
            else:
                if nodo.hijo_der is None:
                    nodo.hijo_der = Elemento(valor_nuevo)
                else:
                    _agregar_aux(nodo.hijo_der, valor_nuevo)

        if self.origen is None:
            self.origen = Elemento(valor)
        else:
            _agregar_aux(self.origen, valor)

    def localizar(self, valor):
        def _localizar_aux(nodo, valor):
            if nodo is None or nodo.valor == valor:
                return nodo
            if valor < nodo.valor:
                return _localizar_aux(nodo.hijo_izq, valor)
            return _localizar_aux(nodo.hijo_der, valor)

        return _localizar_aux(self.origen, valor)

    def retirar(self, valor):
        def _retirar_aux(nodo, valor):
            if nodo is None:
                return None
            if valor < nodo.valor:
                nodo.hijo_izq = _retirar_aux(nodo.hijo_izq, valor)
            elif valor > nodo.valor:
                nodo.hijo_der = _retirar_aux(nodo.hijo_der, valor)
            else:
                if nodo.hijo_izq is None:
                    return nodo.hijo_der
                elif nodo.hijo_der is None:
                    return nodo.hijo_izq
                nodo_siguiente = self._buscar_siguiente(nodo.hijo_der)
                nodo.valor = nodo_siguiente.valor
                nodo.hijo_der = _retirar_aux(nodo.hijo_der, nodo_siguiente.valor)
            return nodo

        self.origen = _retirar_aux(self.origen, valor)

    def _buscar_siguiente(self, nodo):
        actual = nodo
        while actual.hijo_izq is not None:
            actual = actual.hijo_izq
        return actual

    def mostrar_estructura(self, nodo=None, profundidad=0):
        if self.origen is None:
            print("La estructura está vacía.")
            return
        if nodo is None:
            nodo = self.origen
        if nodo is not None:
            if nodo.hijo_der is not None:
                self.mostrar_estructura(nodo.hijo_der, profundidad + 1)
            print("    " * profundidad + str(nodo.valor))
            if nodo.hijo_izq is not None:
                self.mostrar_estructura(nodo.hijo_izq, profundidad + 1)

    def agregar_interactivo(self):
        valor = int(input("Ingrese el valor a agregar: "))
        self.agregar(valor)
        print("Valor agregado.")

    def retirar_interactivo(self):
        valor = int(input("Ingrese el valor a retirar: "))
        self.retirar(valor)
        print("Valor retirado.")

    def localizar_interactivo(self):
        valor = int(input("Ingrese el valor a localizar: "))
        elemento = self.localizar(valor)
        if elemento:
            print(f"Elemento {valor} localizado.")
        else:
            print(f"Elemento {valor} no encontrado.")

    def mostrar_estructura_interactivo(self):
        print("\nEstructura Arbórea:")
        self.mostrar_estructura()

    def interactuar(self):
        print("Estructura Arbórea inicial:")
        self.mostrar_estructura()

        acciones = {
            "1": self.agregar_interactivo,
            "2": self.retirar_interactivo,
            "3": self.localizar_interactivo,
            "4": self.mostrar_estructura_interactivo
        }

        while True:
            print("\nAcciones disponibles:")
            print("1. Agregar")
            print("2. Retirar")
            print("3. Localizar")
            print("4. Mostrar Estructura")
            print("5. Finalizar")

            eleccion = input("Seleccione una acción (1-5): ")

            if eleccion in acciones:
                acciones[eleccion]()
            elif eleccion == "5":
                print("Finalizando el programa.")
                break
            else:
                print("Acción no válida.")

estructura = EstructuraArborea()
estructura.interactuar()
