"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 * Andres Rodriguez - Última version
 """

import sys
from App import logic


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_logic():
    """
    Función que crea una nueva instancia de la lógica

    :return: Nueva instancia de la lógica
    :rtype: logic
    """
    control = logic.new_logic()
    return control


def print_menu():
    """
    Imprime el menú de opciones en consola para el usuario
    """
    print("Opciones:")
    print("1- Cargar Libros")
    print("2- Cargar Tags")
    print("3- Cargar Tags de Libros")
    print("0- Salir")


def load_books(app):
    """
    Función que carga los libros en la aplicación. 
    Carga los libros desde el archivo books.csv y los almacena en la aplicación

    :param app: Aplicación de la lógica
    :type app: logic
    """
    books = logic.load_books(app,
                             "GoodReads/books.csv")
    return books


def load_tags(app):
    """
    Función que carga los tags en la aplicación.
    Carga los tags desde el archivo tags.csv y los almacena en la aplicación

    :param app: Aplicación de la lógica
    :type app: logic
    """
    tags = logic.load_tags(app,
                           "GoodReads/tags.csv")
    return tags


def load_books_tags(app):
    """
    Función que carga los tags de los libros en la aplicación.
    Carga los tags de los libros desde el archivo book_tags.csv y los almacena en la aplicación

    :param app: Aplicación de la lógica
    :type app: logic
    """
    book_tags= logic.load_books_tags(app, "GoodReads/book_tags.csv")
    return book_tags


def first_book(app):
    """
    Devuelve el primer libro cargado en el conjunto de libros
    """
    first = logic.first_book(app)
    return first


def last_book(app):
    """
    Devuelve el último libro cargado en el conjunto de libros
    """
    last = logic.last_book(app)
    return last



# Se crea el controlador asociado a la vista
app = new_logic()

# main del ejercicio


def main():
    """
    Función principal del programa.
    Presenta el menu de opciones y ejecuta las operaciones solicitadas por el usuario.
    """

    working = True
    # ciclo del menu
    while working:
        print_menu()
        inputs = input("Seleccione una opción para continuar\n")
        if int(inputs[0]) == 1:
            print("Cargando información de libros....")
            books = load_books(app)
            print("Total de libros cargados: " + str(books) + "\n")
            
            first = first_book(app)
            print("Primer libro cargado:\n" +str(first['title']) +"\n")
            
            last = last_book(app)
            print("Último libro cargado:\n" + str(last['title']) + "\n")

        elif int(inputs[0]) == 2:
            print("Cargando información de tags....")
            tags = load_tags(app)
            print("Total de tags cargados: " + str(tags) + "\n")

        elif int(inputs[0]) == 3:
            print("Cargando información de Book-Tags..")
            booktags = load_books_tags(app)
            print("Total de Book-Tags cargados: " +str(booktags))

        elif int(inputs[0]) == 0:
            working = False
            print("\nGracias por utilizar el programa.")

        else:
            print("Opcion erronea, vuelva a elegir.\n")
    sys.exit(0)
