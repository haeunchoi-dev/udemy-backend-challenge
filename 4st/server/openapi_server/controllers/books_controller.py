import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.books_book_id_delete200_response import BooksBookIdDelete200Response  # noqa: E501
from openapi_server.models.books_book_id_delete500_response import BooksBookIdDelete500Response  # noqa: E501
from openapi_server.models.books_book_id_get200_response import BooksBookIdGet200Response  # noqa: E501
from openapi_server.models.books_book_id_get404_response import BooksBookIdGet404Response  # noqa: E501
from openapi_server.models.books_book_id_put200_response import BooksBookIdPut200Response  # noqa: E501
from openapi_server.models.books_book_id_put400_response import BooksBookIdPut400Response  # noqa: E501
from openapi_server.models.books_book_id_put_request import BooksBookIdPutRequest  # noqa: E501
from openapi_server.models.books_get200_response import BooksGet200Response  # noqa: E501
from openapi_server.models.books_get500_response import BooksGet500Response  # noqa: E501
from openapi_server.models.books_post201_response import BooksPost201Response  # noqa: E501
from openapi_server.models.books_post400_response import BooksPost400Response  # noqa: E501
from openapi_server.models.books_post_request import BooksPostRequest  # noqa: E501
from openapi_server import util

import alchemy.book

def books_book_id_delete(book_id):  # noqa: E501
    """Delete book information

     # noqa: E501

    :param book_id: 삭제할 책의 고유 ID
    :type book_id: 

    :rtype: Union[BooksBookIdDelete200Response, Tuple[BooksBookIdDelete200Response, int], Tuple[BooksBookIdDelete200Response, int, Dict[str, str]]
    """
    success = alchemy.book.delete(book_id)
    if success:
        return BooksBookIdDelete200Response(status=200), 200
    else:
        return BooksBookIdDelete500Response(status=500, code="BOOK_DELETION_FAILED", message="Failed to delete book information"), 500


def books_book_id_get(book_id):  # noqa: E501
    """Get book information by ID

     # noqa: E501

    :param book_id: 조회할 책의 고유 ID
    :type book_id: 

    :rtype: Union[BooksBookIdGet200Response, Tuple[BooksBookIdGet200Response, int], Tuple[BooksBookIdGet200Response, int, Dict[str, str]]
    """
    book = alchemy.book.read_one(book_id)
    if book:
        return BooksBookIdGet200Response(status=200, data=book), 200
    else:
        return BooksBookIdGet404Response(status=404, code="BOOK_NOT_FOUND", message="Book not found"), 404


def books_book_id_put(book_id):  # noqa: E501
    """Update book information

     # noqa: E501

    :param book_id: 갱신할 책의 고유 ID
    :type book_id: 
    :param books_book_id_put_request: 
    :type books_book_id_put_request: dict | bytes

    :rtype: Union[BooksBookIdPut200Response, Tuple[BooksBookIdPut200Response, int], Tuple[BooksBookIdPut200Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        books_book_id_put_request = BooksBookIdPutRequest.from_dict(connexion.request.get_json())  # noqa: E501

    updated_book = alchemy.book.update(book_id, **books_book_id_put_request.to_dict())
    if updated_book:
        return BooksBookIdPut200Response(status=200, data=updated_book), 200
    else:
        return BooksBookIdPut400Response(status=400, code="BOOK_UPDATE_INVALID_DATA", message="Invalid input data"), 400


def books_get(page, size, sort=None, direction=None, genre=None):  # noqa: E501
    return alchemy.book.read_all(page, size, sort, direction, genre)


def books_post():  # noqa: E501
    """Create a new book

     # noqa: E501

    :param books_post_request: 
    :type books_post_request: dict | bytes

    :rtype: Union[BooksPost201Response, Tuple[BooksPost201Response, int], Tuple[BooksPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        books_post_request = BooksPostRequest.from_dict(connexion.request.get_json())  # noqa: E501

    new_book = alchemy.book.create(
        title=books_post_request.title,
        author=books_post_request.author,
        publishedDate=books_post_request.published_date,
        publisher=books_post_request.publisher,
        price=books_post_request.price,
        genre=books_post_request.genre,
        description=books_post_request.description
    )
    return BooksPost201Response(status=201, data=new_book), 201
