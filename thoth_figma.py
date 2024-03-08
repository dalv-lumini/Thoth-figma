from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

preguntas = []  # Lista para almacenar las preguntas y respuestas

@app.route('/')
def index():
    return render_template('index.html', preguntas=preguntas)

@app.route('/buscar', methods=['POST'])
def buscar():
    pregunta = request.form['pregunta']
    
    # Agregar una animación de "buscando" antes de enviar la solicitud
    preguntas.append({'pregunta': pregunta, 'respuesta': 'Buscando...'})

    api_url = 'http://127.0.0.1:5000/pergunta/' + pregunta
    response = requests.get(api_url)
    data = response.json()
   
    preguntas[-1]['respuesta'] = data['resposta']  # Actualizar la respuesta en la lista
    return render_template('index.html', preguntas=preguntas)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
