import pickle
import os.path
from os import path

class user:
    def __init__(self, estado, nombre, usuario, contrasena):
        self.estado = estado
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena

    def __str__(self):
        return "\nID de estado: " + str(self.estado) + "\nNombre: " \
               + str(self.nombre) + "\nUsuario: " + str(self.usuario) \
               + "\nContrasena: " + str(self.contrasena) + "\n"

def capturar(estado):
    pickle_out = open("estado.pickle", "wb")
    pickle.dump(estado, pickle_out)
    pickle_out.close()

def restaurar():
    pickle_in = open("estado.pickle", "rb")
    estado = pickle.load(pickle_in)
    pickle_in.close()
    return estado

def respaldar(lista):
    pickle_out = open("respaldo.pickle", "wb")
    pickle.dump(lista, pickle_out)
    pickle_out.close()

def cargar(objetos):
    pickle_in = open("respaldo.pickle", "rb")
    objetos = pickle.load(pickle_in)
    pickle_in.close()
    return objetos

def main():
    lista=[]

    filepath = "respaldo.pickle"
    if not path.exists(filepath):
        print ("Aun no hay usuarios guardados en el sistema...\n"
               " ¿Quieres ingresar un nuevo usuario? (Y/N)")
        opcion = input()

        if opcion == 'Y':
            nombre = input("Nombre: ")
            estado = user(1, nombre, None, None)
            capturar(estado)

            usuario = input("Nombre de usuario: ")
            estado = user(2, nombre, usuario, None)
            capturar(estado)

            contrasena = input("Contrasena: ")
            estado = user(3, nombre, usuario, contrasena)
            capturar(estado)

            lista.append(estado)
            respaldar(lista)

        elif opcion == 'N':
            print("Hasta luego!... ")
            os.system("pause")
            raise SystemExit
        else:
            print("Opcion invalida")
            main()

    lista = cargar(lista)

    while (True):

        obj = restaurar()

        if obj.estado == 3:

            print("\n--- MENU ---")
            print("1) Capturar nuevo usuario")
            print("2) Mostrar lista de usuarios")
            print("3) Salir del programa\n")
            opcion = int(input())

            if opcion == 1:
                nombre = input("Nombre: ")
                estado = user(1, nombre, None, None)
                capturar(estado)

                usuario = input("Nombre de usuario: ")
                estado = user(2, nombre, usuario, None)
                capturar(estado)

                contrasena = input("Contrasena: ")
                estado = user(3, nombre, usuario, contrasena)
                capturar(estado)

                lista.append(estado)
                respaldar(lista)

            elif opcion == 2:
                print("--- Lista de usuarios ---")
                for ele in lista:
                    print(ele)

            elif opcion == 3:
                print("Hasta luego!... ")
                os.system("pause")
                break

            else:
                print("Opcion invalida")

        elif obj.estado == 2:
            print("Campos recuperados:\nNombre: " + obj.nombre
                  + "\nUsuario: " + obj.usuario)

            contrasena = input("Contrasena: ")
            estado = user(3, obj.nombre, obj.usuario, contrasena)
            capturar(estado)

            lista.append(estado)
            respaldar(lista)

        elif obj.estado == 1:
            print("Campos recuperados:\nNombre: " + obj.nombre)

            usuario = input("Nombre de usuario: ")
            estado = user(2, obj.nombre, usuario, None)
            capturar(estado)

            contrasena = input("Contrasena: ")
            estado = user(3, obj.nombre, usuario, contrasena)
            capturar(estado)

            lista.append(estado)
            respaldar(lista)

main()