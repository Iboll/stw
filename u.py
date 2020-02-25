from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def deviz():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promo():
    text = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!', 'Присоединяйся!']
    return '</br>'.join(text)


@app.route('/image_mars')
def im():
    return '''<!doctype html>
                       <html lang="en">
                         <head>
                           <meta charset="utf-8">
                           <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet" 
                           href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                           integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                           crossorigin="anonymous">
                           <title>Привет, Марс!</title>
                         </head>
                           <title>Привет, Марс!</title>
                         </head>
                         <body>
                           <h1>Жди нас, Марс!</h1>''' +\
                          '''<img src="{}" alt="здесь должна была быть картинка, 
                         но не нашлась">'''.format(url_for('static', filename='img/mars.jpg')) + '''
                            <div>
                               Вот она какая, красная планета.
                            </div>
                          </body>
                          </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
