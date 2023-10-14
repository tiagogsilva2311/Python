from flask import Flask, render_template # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/success')
def success():
    return 'Success'

@app.route('/hello/<string:girlfriend>/<int:num>')
def girlfriend(girlfriend,num):   
    return render_template("girlfriend.html",girlfriend=girlfriend, num=num)

#Las rutas siempre van arriba de esto
if __name__ == '__main__':
    app.run(debug=True)



