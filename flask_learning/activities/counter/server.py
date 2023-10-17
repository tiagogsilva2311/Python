from flask import Flask, render_template, request, redirect, session # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
app.secret_key= '123'
@app.route('/')
def board():
    if "count" in session:
        session['count'] +=1
        return render_template('index.html')
    else: 
        session['count']=0
        return render_template('index.html')


@app.route('/count', methods=['POST'])
def count():
    if "count" in session:
        session['count'] +=1
        return redirect('/')
    else: 
        session['count']=0
        return redirect('/')

@app.route('/destroy', methods=['POST'])
def destroy():
    session.clear()
    return redirect('/')



#Las rutas siempre van arriba de esto
if __name__ == '__main__':
    app.run(debug=True)