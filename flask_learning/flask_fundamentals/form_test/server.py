from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'mortiz'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['username'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')

@app.route('show')
def show_user():
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])


#Rutas Arriba de esto
if __name__ == '__main__':
    app.run(debug= True)