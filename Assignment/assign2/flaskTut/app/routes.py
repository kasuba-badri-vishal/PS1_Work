from flask import render_template,flash,redirect,url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    # return "Hello World!"
    user = { 'username':'Badri'}
    posts = [
        {
            'author': {'username': 'Tushar'},
            'body': 'Beautiful day in Goa!'
        },
        {
            'author': {'username': 'Rohith'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    # return '''
    # <html>
    #     <head>
    #         <title>flaskTut</title>
    #     </head>
    #     <body>
    #         <h1>Hello,''' + user['username'] + '''!</h1>
    #     </body>
    # </html>  '''
    return render_template('index.html',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In',form = form)
