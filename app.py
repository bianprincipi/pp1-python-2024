from flask import Flask, render_template, request
import requests
app = Flask(__name__)

listado_personas = [
    dict(
        name=dict(
            first="Juan Pablo",
            last="Varsky",
        ),
        location=dict(
            city="Los Angeles"
        ),
        email="jpv@gmail.com"
        ),
    dict(
        name=dict(
            first="Pablo Juan",
            last="Perez",
        ),
        location=dict(
            city="Tosquita"
        ),
        email="pjp@gmail.com"
        ),
]

@app.route('/') # app es la instancia, route el metodo, '/' es el disparador
def index():
    return render_template(
        'index.html',
    )

@app.route('/info') # app es la instancia, route el metodo, '/' es el disparador
def informacion():
    return render_template(
        'informacion.html',
    )

@app.route('/bienvenido/<nombre>')
def bienvenida(nombre):
    return render_template(
        'bienvenida.html',
    )

@app.route('/personas')
def personas():
    listado = listado_personas
    return render_template(
        'personas.html',
        listado = listado
    )

@app.route ('/personas_add', methods=["POST", "GET"])
def agregar_personas():
        if request.method == 'POST':
                        #peticion-formulario-clave
            first_name = request.form['nombre']
            last_name = request.form['apellido']
            city = request.form['ciudad']
            email = request.form['email']
            
            persona=dict(
                name=dict(
                    first=first_name,
                    last=last_name,
                ),
                location=dict(
                    city=city,
                ),
                email=email,
            )
            listado_personas.append(persona)
        return render_template ('add_personas.html')
