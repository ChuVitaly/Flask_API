from flask import Flask, jsonify, request

app = Flask(__name__)

# Фейковая база данных для объявлений
ads_database = [
    {'id': 1, 'title': 'Продам автомобиль', 'description': 'Отличный автомобиль, 100000 км пробега', 'price': '50000'},
    {'id': 2, 'title': 'Продам ноутбук', 'description': 'Мощный ноутбук, отличное состояние', 'price': '800'},
    {'id': 3, 'title': 'Сдам квартиру', 'description': 'Уютная квартира в центре города', 'price': '20000'},
    # Дополнительные объявления можно добавить здесь
]


# Получение списка всех объявлений
@app.route('/ads', methods=['GET'])
def get_all_ads():
    return jsonify(ads_database)


# Получение конкретного объявления по ID
@app.route('/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    ad = next((ad for ad in ads_database if ad['id'] == ad_id), None)
    if ad:
        return jsonify(ad)
    return jsonify({'message': 'Объявление не найдено'}), 404


# Создание нового объявления
@app.route('/ads', methods=['POST'])
def create_ad():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    price = data.get('price')
    if title and description and price:
        new_ad = {'id': len(ads_database) + 1, 'title': title, 'description': description, 'price': price}
        ads_database.append(new_ad)
        return jsonify(new_ad), 201
    return jsonify({'message': 'Не удалось создать объявление'}), 400


# Удаление объявления по ID
@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    ad = next((ad for ad in ads_database if ad['id'] == ad_id), None)
    if ad:
        ads_database.remove(ad)
        return jsonify({'message': 'Объявление успешно удалено'})
    return jsonify({'message': 'Объявление не найдено'}), 404


if __name__ == '__main__':
    app.run()
