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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 * Santiago Arteaga - Otras versiones
 * Andres Rodriguez - Última version
 """

import csv
import os

# Importar el modulo de la estructura de datos set
from DataStructures import Set as set

# Directorio de datos de los archivos
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

"""
La lógica se encarga de procesar los datos y realizar las operaciones
sobre ellos. En este caso, se encarga de cargar los datos y realizar
las consultas sobre ellos.
"""


def new_logic():
    """
    Inicializa los datos y crea un catalogo vacio. 

    Para esta actividad, un catalogo es un diccionario donde se guardan
    las estructuras de datos que representan los libros, los autores, los
    generos y la asociación entre libros y generos. 

    Se crea un catalogo con las siguientes atributos:
    - books: Set para guardar los libros.
    - tags: Set para guardar los generos.
    - book_tags: Set para guardar la asociación entre libros y generos.

    :return: Catalogo inicializado
    :rtype: dict
    """

    # Creación del catalogo vacio
    catalog = {
        "books": None,
        "tags": None,
        "book_tags": None
    }

    # Inicialización de las estructuras de datos
    catalog["books"] = set.new_set()
    catalog["tags"] = set.new_set()
    catalog["book_tags"] = set.new_set()

    return catalog


# Funciones para la carga de datos

def load_books(catalog, filename):
    """
    Función que carga los libros en el catalogo.

    Por cada libro se toman sus autores y por cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict
    :param filename: Nombre del archivo csv con los libros
    :type filename: str

    :returns: Tamaño del conjunto de libros
    :rtype: int
    """
    books = catalog["books"]
    books_file = os.path.join(data_dir, filename)
    catalog["books"] = set.load_set(books, books_file)
    return book_size(catalog)


def load_tags(catalog, filename):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags

    :param catalog: Catalogo de la aplicación
    :type catalog: dict
    :param filename: Nombre del archivo csv con los tags
    :type filename: str

    :returns: Tamaño del conjunto de tags
    :rtype: int
    """
    tags_file = os.path.join(data_dir, filename)
    input_file = csv.DictReader(open(tags_file, encoding="utf-8"))
    catalog["tags"] = set.new_set()

    for tag in input_file:
        set.add_element(catalog["tags"], tag)

    return tag_size(catalog)


def load_books_tags(catalog, filename):
    """
    Carga los tags de los libros del archivo y los agrega a la lista
    de tags. Siga el mismo procedimiento que en la carga de libros.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict
    :param filename: Nombre del archivo csv con los tags de los libros
    :type filename: str

    :returns: Tamaño del conjunto de tags de los libros
    :rtype: int
    """
    book_tags_file= os.path.join(data_dir, filename)
    input_file=csv.DictReader(open(book_tags_file, encoding="utf-8"))
    catalog["book_tags"]= set.new_set()
    for book_tag in input_file:
        set.add_element(catalog["book_tags"], book_tag)
    return book_tag_size(catalog)


def first_book(catalog):
    """
    Devuelve el primer libro del catalogo
    """
    return set.get_first_element(catalog["books"])


def last_book(catalog):
    """
    Devuelve el ultimo libro del catalogo
    """
    return set.get_last_element(catalog["books"])

# Funciones para la manipulacion de los datos


def add_book_tags_file(catalog, booktagsfile):
    """
    Esta funcion guardar los booktags provenientes del archivo CSV.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict
    :param booktagsfile: Nombre del archivo csv con los booktags
    :type booktagsfile: str

    :returns: catalog
    :rtype: dict
    """
    bt = set.load_set(set.new_set(), booktagsfile)
    catalog["book_tags"] = bt
    return catalog


def create_book_tag_list(catalog):
    """
    Esta funcion crea una lista vacia para booktags.
    """
    catalog["book_tags"] = set.new_set()
    return catalog


def add_book_tag(catalog, booktag):
    """
    Esta funcion agrega un elemento a lista de booktags.

    :param catalog: Catalogo de la aplicación
    :type catalog: dict
    :param booktag: Tag a agregar
    :type booktag: dict

    :returns: catalog
    :rtype: dict
    """
    set.add_element(catalog["book_tags"], booktag)
    return catalog


# Funciones de consulta

def book_size(catalog):
    return set.size(catalog["books"])


def tag_size(catalog):
    return set.size(catalog["tags"])


def book_tag_size(catalog):
    return set.size(catalog["book_tags"])