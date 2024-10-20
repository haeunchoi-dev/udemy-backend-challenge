from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.books_book_id_put200_response_data import BooksBookIdPut200ResponseData
from openapi_server import util

from openapi_server.models.books_book_id_put200_response_data import BooksBookIdPut200ResponseData  # noqa: E501

class BooksBookIdPut200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status=None, data=None):  # noqa: E501
        """BooksBookIdPut200Response - a model defined in OpenAPI

        :param status: The status of this BooksBookIdPut200Response.  # noqa: E501
        :type status: float
        :param data: The data of this BooksBookIdPut200Response.  # noqa: E501
        :type data: BooksBookIdPut200ResponseData
        """
        self.openapi_types = {
            'status': float,
            'data': BooksBookIdPut200ResponseData
        }

        self.attribute_map = {
            'status': 'status',
            'data': 'data'
        }

        self._status = status
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'BooksBookIdPut200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _books__bookId__put_200_response of this BooksBookIdPut200Response.  # noqa: E501
        :rtype: BooksBookIdPut200Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self) -> float:
        """Gets the status of this BooksBookIdPut200Response.


        :return: The status of this BooksBookIdPut200Response.
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status: float):
        """Sets the status of this BooksBookIdPut200Response.


        :param status: The status of this BooksBookIdPut200Response.
        :type status: float
        """

        self._status = status

    @property
    def data(self) -> BooksBookIdPut200ResponseData:
        """Gets the data of this BooksBookIdPut200Response.


        :return: The data of this BooksBookIdPut200Response.
        :rtype: BooksBookIdPut200ResponseData
        """
        return self._data

    @data.setter
    def data(self, data: BooksBookIdPut200ResponseData):
        """Sets the data of this BooksBookIdPut200Response.


        :param data: The data of this BooksBookIdPut200Response.
        :type data: BooksBookIdPut200ResponseData
        """

        self._data = data
