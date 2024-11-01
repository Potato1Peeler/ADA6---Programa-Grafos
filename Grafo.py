class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = {}

    def agregar_arista(self, v1, v2, costo):
        if v1 not in self.grafo or v2 not in self.grafo:
            raise ValueError(f"Estado no encontrado")
        self.grafo[v1][v2] = costo
        self.grafo[v2][v1] = costo  

    def mostrar_relaciones(self):
        for v1 in self.grafo:
            print(f"\nEstado: {v1}")
            for v2, costo in self.grafo[v1].items():
                print(f"  - Tiene relación con {v2} [costo: {costo}]")

    def recorrer_sin_repetir(self):
        visitados = set()
        recorrido = []
        costo_total = 0

        def busqueda(vertice):
            nonlocal costo_total
            visitados.add(vertice)
            recorrido.append(vertice)
            for vecino, costo in self.grafo[vertice].items():
                if vecino not in visitados:
                    costo_total += costo
                    busqueda(vecino)

        if self.grafo:
            busqueda(next(iter(self.grafo)))

        return " ---> ".join(recorrido), costo_total

    def recorrer_con_repeticion(self):
        recorrido = []
        costo_total = 0
        estado_anterior = None
        for v1 in self.grafo:
            recorrido.append(v1)
            if estado_anterior is not None:
                costo_total += self.grafo[estado_anterior][v1]

            if v1 in ["Zacatecas", "Chihuahua"]:
                if estado_anterior is not None:
                    recorrido.append(estado_anterior)
                    costo_total += self.grafo[v1][estado_anterior]
                estado_anterior = v1
                continue
            estado_anterior = v1

        return " ---> ".join(recorrido), costo_total


g = Grafo()
estados = ["Baja California Sur", "Baja California", "Sonora", "Chihuahua", "Coahuila", "Durango", "Zacatecas"]

for estado in estados:
    g.agregar_vertice(estado)

g.agregar_arista("Baja California Sur", "Baja California", 25)
g.agregar_arista("Baja California", "Sonora", 100)
g.agregar_arista("Sonora", "Chihuahua", 40)
g.agregar_arista("Chihuahua", "Coahuila", 35)
g.agregar_arista("Coahuila", "Durango", 10)
g.agregar_arista("Durango", "Zacatecas", 75)

print("\n---Relaciones entre estados y costos---")
g.mostrar_relaciones()

recorrido_sin_repetir, costo_sin_repetir = g.recorrer_sin_repetir()
print("\nRecorrido sin repetir ningún estado:", recorrido_sin_repetir)
print("El recorrido completo tiene como costo total:", costo_sin_repetir)

recorrido_repeticion, costo_repeticion = g.recorrer_con_repeticion()
print("\nRecorrido repitiendo al menos un estado:", recorrido_repeticion)
print("El recorrido completo tiene como costo total:", costo_repeticion)
