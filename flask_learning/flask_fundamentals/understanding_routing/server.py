from flask import Flask # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/dojo')
def success():
    return 'DOJO!!'

@app.route('/say/<string:name>')
def say(name):   
    return f"<p>Hola {name.capitalize()}!</p>"

@app.route ('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    output = ''
    
    for i in range(0,num):
        output += f"<p>{word.capitalize()}</p>"

    return output

#Las rutas siempre van arriba de esto
if __name__ == '__main__':
    app.run(debug=True)