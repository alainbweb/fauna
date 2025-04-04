
from lista_animales import ListaAnimales
from perro import Perro
from gato import Gato

class Menu:
    def __init__(self):
        self.lista_animales = ListaAnimales()


    def mostrar_menu(self):
        while True:
            print("\n---- Menú ----")
            print("1. Mostrar lista de animales")
            print("2. Agregar nuevo perro")
            print("3. Agregar nuevo gato")
            print("4. Salir")

            opcion = input("Inserta una opción: ")

            if opcion == "1":
                self.lista_animales.mostrar_animales()
            elif opcion == "2":
                nombre = input("Nombre del perro: ")
                edad = int(input("Edad del perro: "))
                self.lista_animales.agregar_animal(Perro(nombre, edad))
                print("Perro agregado correctamente.")
            elif opcion == "3":
                nombre = input("Nombre del gato: ")
                edad = int(input("Edad del gato: "))
                self.lista_animales.agregar_animal(Gato(nombre, edad))
                print("Gato agregado correctamente.")
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")