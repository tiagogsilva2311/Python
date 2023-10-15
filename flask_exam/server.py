from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'mortiz'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['last_name']=request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm_password']= request.form['confirm_password']
    return redirect('/user')

@app.route('/user')
def show_user():
    return render_template('show.html', name_on_template=session['name'], email_on_template=session['email'], last_name_on_template=session['last_name'])


#Rutas Arriba de esto
if __name__ == '__main__':
    app.run(debug= True)