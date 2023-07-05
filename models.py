from pony import orm
from datetime import datetime
from pony.orm import Database, Required

db = Database()

# Создайте соединение с базой данных
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)


class Declaration(db.Entity):
    title = Required(str)
    description = Required(str)
    author = Required(str)
    created_at = Required(datetime, default=datetime.now)


db.generate_mapping(create_tables=True)
