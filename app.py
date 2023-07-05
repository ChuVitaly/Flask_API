from flask import Flask, render_template, request, redirect
from pony import orm
from pony.orm import Database
from models import Declaration

app = Flask(__name__)

db = Database()

# соединение с базой данных
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


@app.route('/index')
@orm.db_session
def index():
    ads = orm.select(a for a in Declaration)[:10]
    return render_template('index.html', ads=ads)


@app.route('/create_ad', methods=['GET', 'POST'])
@orm.db_session
def create_ad():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        author = request.form['author']
        created_at = request.form['created_at']
        ad = Declaration(title=title, description=description, author=author, created_at=created_at)
        orm.commit()
        return redirect('/index')
    return render_template('create_ad.html')


if __name__ == '__main__':
    app.run()
