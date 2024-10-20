from config import db
from sqlalchemy import asc, desc  
from alchemy.models import Book, book_schema, books_schema

import logging
logging.basicConfig()
logger = logging.getLogger('sqlalchemy.engine')
logger.setLevel(logging.DEBUG)

def read_all(page=1, per_page=10, sort=None, direction=None, genre=None):
    query = Book.query

    if genre:
        query = query.filter(Book.genre == genre)

    if sort:
        if direction == "desc":
            query = query.order_by(desc(getattr(Book, sort)))
        else:
            query = query.order_by(asc(getattr(Book, sort)))

    books = query.paginate(page=page, per_page=per_page, error_out=False)

    return {
        "page": {
            "currentPage": books.page,
            "pageSize": books.per_page,
            "totalBooks": books.total,
            "totalPages": books.pages,
        },
        "books": books_schema.dump(books.items)
    }


def read_one(id):
    book = Book.query.filter(Book.id == id).one_or_none()

    if book is not None:
        return book_schema.dump(book)
    else:
        return None


def create(title, author, publishedDate, publisher, price, genre, description):
    new_book = Book(
        title=title,
        author=author,
        publishedDate=publishedDate,
        publisher=publisher,
        price=price,
        genre=genre,
        description=description
    )
    db.session.add(new_book)
    db.session.commit()
    return book_schema.dump(new_book)


def update(id, title=None, author=None, published_date=None, publisher=None, price=None, genre=None, description=None):
    existing_book = Book.query.filter(Book.id == id).one_or_none()

    if existing_book:
        if title:
            existing_book.title = title
        if author:
            existing_book.author = author
        if published_date:
            existing_book.publishedDate = published_date
        if publisher:
            existing_book.publisher = publisher
        if price:
            existing_book.price = price
        if genre:
            existing_book.genre = genre
        if description:
            existing_book.description = description

        db.session.merge(existing_book)
        db.session.commit()
        return book_schema.dump(existing_book)
    else:
        return None


def delete(id):
    existing_book = Book.query.filter(Book.id == id).one_or_none()

    if existing_book:
        db.session.delete(existing_book)
        db.session.commit()
        return True
    else:
        return False
