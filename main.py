#  REST API (backend) для сайта объявлений.

from flask import Flask, request, jsonify, json
from pony.orm import Database, Required, db_session, select

db = Database()


class Declaration(db.Entity):
    title = Required(str)
    description = Required(str)
    author = Required(str)
    created_at = Required(str)


db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

app = Flask(__name__)


@app.route('/declarations', methods=['GET'])
@db_session
def get_declarations():
    ads = select(a for a in Declaration)[:]
    response_data = {'declarations': [ad.to_dict() for ad in ads]}
    response = app.response_class(
        response=json.dumps(response_data, ensure_ascii=False),
        status=200,
        mimetype='application/json; charset=utf-8'
    )
    return response


@app.route('/declarations', methods=['POST'])
@db_session
def create_declaration():
    data = request.json
    ad = Declaration(
        title=data['title'],
        description=data['description'],
        author=data['author'],
        created_at=data['created_at']
    )
    return jsonify({'message': 'Обьявление создано успешно'})


@app.route('/declarations/<int:ad_id>', methods=['PUT'])
@db_session
def update_declaration(ad_id):
    data = request.json
    ad = Declaration.get(id=ad_id)
    if not ad:
        return jsonify({'error': 'Обьявление не найдено'})
    ad.title = data['title']
    ad.description = data['description']
    ad.author = data['author']
    ad.created_at = data['created_at']
    return jsonify({'message': 'Обьявление обновлено'})


@app.route('/declaration/<int:ad_id>', methods=['DELETE'])
@db_session
def delete_declaration(ad_id):
    ad = Declaration.get(id=ad_id)
    if not ad:
        return jsonify({'error': 'Обьявление не найдено'})
    ad.delete()
    return jsonify({'message': 'Обьявление удалено'})


if __name__ == '__main__':
    app.run(debug=True)
