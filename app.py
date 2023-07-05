from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Фейковая база данных для объявлений
ads_database = [
    {'title': 'Продам автомобиль', 'description': 'Отличный автомобиль, 100000 км пробега', 'price': '50000'},
    {'title': 'Продам ноутбук', 'description': 'Мощный ноутбук, отличное состояние', 'price': '800'},
    {'title': 'Сдам квартиру', 'description': 'Уютная квартира в центре города', 'price': '20000'},
    # Дополнительные объявления можно добавить здесь
]


@app.route('/')
def index():
    return render_template('index.html', ads=ads_database)


@app.route('/create_ad', methods=['GET', 'POST'])
def create_ad():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = request.form['price']
        ad = {'title': title, 'description': description, 'price': price}
        ads_database.append(ad)
        return redirect('/')
    return render_template('create_ad.html')


if __name__ == '__main__':
    app.run()
