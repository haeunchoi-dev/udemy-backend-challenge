from config import db
from config import ma

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author = db.Column(db.String(128))
    publishedDate = db.Column(db.String(128))
    publisher = db.Column(db.String(128))
    price = db.Column(db.Integer)
    genre = db.Column(db.String(128))
    description = db.Column(db.String(256))

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session


book_schema = BookSchema()
books_schema = BookSchema(many=True)
