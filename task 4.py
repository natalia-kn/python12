from flask import Flask, redirect, request, render_template, flash, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_main.html')


@app.route('/login', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')  # Запит до даних форм
        password = request.form.get('password')
        if username == 'user' and password == 'user':
            message = "Авторизовано"
        else:
            message = "Помилка при авторизації"
    return render_template('login.html', message=message)


@app.route('/about')
def index_about():
    return render_template('about.html')


@app.route('/album')
def index_album():
    return render_template('album.html')


@app.route('/history')
def index_history():
    return render_template('history.html')

@app.route('/third')
def index_third():
    return render_template('third_album.html')



if __name__ == "__main__":
    app.run(debug=True)
