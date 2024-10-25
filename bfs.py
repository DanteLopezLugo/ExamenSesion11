class AlgoritmosBusqueda:
    '''
    Inicio
    '''    
    def __init__(self,grafo=[], objetivo=None):
        self.grafo = grafo
        self.objetivo = objetivo
       
    '''
    Algoritmo DFS
    '''
    def DFS(self):
        cola = [self.objetivo]
        rama_visitada = []
        while cola:
            posicion_rama = cola.pop()
            if posicion_rama not in rama_visitada:
                rama_visitada.append(posicion_rama)
            for rama in self.grafo[posicion_rama]:
                if rama not in rama_visitada:
                    cola.append(rama)
        return rama_visitada
 
    '''
    Algoritmo DFS
    '''
    def BFS(self):
        cola = [self.objetivo]
        rama_visitada = [self.objetivo]
        while cola:
            posicion_rama = cola.pop(0)
            for rama in self.grafo[posicion_rama]:
                if rama not in rama_visitada:
                    cola.append(rama)
                    rama_visitada.append(rama)
        return rama_visitada
    
grafo = {"A":["L","N","M"],"L":["H","F"],"M":["K","G"],"N":[],"H":["E"],"E":[],"F":["O"],"O":["I"],"I":[],"G":["D"],"D":["B"],"B":[],"K":["J","G"],"J":[],"G":[]}
#grafo = {"A":["L","N","M"],"L":["H","F"],"M":["K","G"],"N":[],"H":["E"],"E":[],"F":["O"],"O":["I"],"I":[],"G":["D"],"D":["B"],"B":[],"K":["J","G"],"J":[],"G":[]}
a = AlgoritmosBusqueda(grafo, "A")

print(a.BFS())