from flask import Flask, render_template # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')
def board():
    return render_template('index.html')

@app.route('/<int:x>')
def shiny(x):
    return render_template('alternate.html', x=x)

@app.route('/<int:x>/<int:y>')
def dual(x,y):
    return render_template('dual.html',x=x, y=y)





#Las rutas siempre van arriba de esto
if __name__ == '__main__':
    app.run(debug=True)