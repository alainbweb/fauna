
class listaGenerica():
    def __init__(self):
        self.lista = []

def agregar_T(self, T):
    
    self.lista.append(T)
        
def eliminar_T(self,T):
    if T in self.lista:
        self.lista.remove(T)
    else:
        print("Elemento no encontrado en la lista.")            

def busar_T(self, T):
    if(existe_T(T)):
        return lista.index(T)

def exite_T(T):
    if T in self.lista:
        return True
    else:
        return False

def mostrar_lista(self):
        print("Lista:")
        for i, elemento in enumerate(self.lista, 1):
            print(f"{i}. {elemento}")
        

    