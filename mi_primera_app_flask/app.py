from flask import Flask
from data.data_productos import categorias, productos

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>¡Hola! Soy Jonathan Gorostiaga. ¡Y estoy aprendiendo a usar Flask para crear aplicaciones web geniales!</h1>"

@app.route('/productos')
def listar_productos():
    lista_de_productos_str = "<h1>MI LISTA DE PRODUCTOS</h1>"
    
    for producto in productos:

        lista_de_productos_str += f"ID: {producto['id']}, Descripción: {producto['descripcion']}, Categoría ID: {producto['categoria_id']}<br>"
        
    return lista_de_productos_str


@app.route('/categorias')
def listar_categorias():
    listar_categorias_str="<h1>Listado de categorias</h1>"
    for categoria in categorias:
        listar_categorias_str+=f"ID:{categoria['id']}, Descripcion: {categoria['descripcion']}<br>"
    return listar_categorias_str