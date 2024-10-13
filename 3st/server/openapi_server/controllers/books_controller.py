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


def books_book_id_delete(book_id):  # noqa: E501
    """Delete book information

     # noqa: E501

    :param book_id: 삭제할 책의 고유 ID
    :type book_id: 

    :rtype: Union[BooksBookIdDelete200Response, Tuple[BooksBookIdDelete200Response, int], Tuple[BooksBookIdDelete200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def books_book_id_get(book_id):  # noqa: E501
    """Get book information by ID

     # noqa: E501

    :param book_id: 조회할 책의 고유 ID
    :type book_id: 

    :rtype: Union[BooksBookIdGet200Response, Tuple[BooksBookIdGet200Response, int], Tuple[BooksBookIdGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def books_book_id_put(book_id, books_book_id_put_request):  # noqa: E501
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
    return 'do some magic!'


def books_get(page, size, sort=None, direction=None, genre=None):  # noqa: E501
    """Get a list of books

     # noqa: E501

    :param page: 페이지 번호
    :type page: 
    :param size: 한 페이지 당 책의 수
    :type size: 
    :param sort: 정렬 기준
    :type sort: str
    :param direction: 정렬 방향
    :type direction: str
    :param genre: 장르 필터링
    :type genre: str

    :rtype: Union[BooksGet200Response, Tuple[BooksGet200Response, int], Tuple[BooksGet200Response, int, Dict[str, str]]
    """
    return 'do some magic!'


def books_post(books_post_request):  # noqa: E501
    """Create a new book

     # noqa: E501

    :param books_post_request: 
    :type books_post_request: dict | bytes

    :rtype: Union[BooksPost201Response, Tuple[BooksPost201Response, int], Tuple[BooksPost201Response, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        books_post_request = BooksPostRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
