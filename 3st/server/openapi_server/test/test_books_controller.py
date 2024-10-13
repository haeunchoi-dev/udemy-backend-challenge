import unittest

from flask import json

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
from openapi_server.test import BaseTestCase


class TestBooksController(BaseTestCase):
    """BooksController integration test stubs"""

    def test_books_book_id_delete(self):
        """Test case for books_book_id_delete

        Delete book information
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books/{book_id}'.format(book_id=3.4),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_book_id_get(self):
        """Test case for books_book_id_get

        Get book information by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books/{book_id}'.format(book_id=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_book_id_put(self):
        """Test case for books_book_id_put

        Update book information
        """
        books_book_id_put_request = openapi_server.BooksBookIdPutRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/books/{book_id}'.format(book_id=1),
            method='PUT',
            headers=headers,
            data=json.dumps(books_book_id_put_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_get(self):
        """Test case for books_get

        Get a list of books
        """
        query_string = [('page', 1),
                        ('size', 10),
                        ('sort', 'title'),
                        ('direction', 'asc'),
                        ('genre', 'IT')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/books',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_books_post(self):
        """Test case for books_post

        Create a new book
        """
        books_post_request = openapi_server.BooksPostRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/books',
            method='POST',
            headers=headers,
            data=json.dumps(books_post_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
