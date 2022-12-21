import requests
import logging
from requests.auth import HTTPBasicAuth

from pymailbaby import exceptions
from pymailbaby.helpers import *

__version__ = "1.0.5"


logger = logging.getLogger(__name__)

class Client(object):
    """
    Mail.baby interface.
    """

    def __init__(
            self,
            api_key,
            order_id="",
            baseurl="https://api.mailbaby.net",
            ssl_verify=True):
        """
        Create a new instance.
        Args:
            account_id (str): The account_id for the Mail.baby credentials. ** required **
            api_key (str): The api_key of the Mail.baby credentials. ** required **
        """
        self.api_key = api_key
        self.baseurl = baseurl
        self.ssl_verify = ssl_verify
        self.headers = {
            'User-Agent': 'pymailbaby v' + __version__,
            'X-API-KEY': self.api_key
        }
        self.order_id = order_id
        self.default_params = {'id': self.order_id}

    def call(self, method="get", endpoint=None,
             **params) -> dict:

        response = requests.request(method=method,
                                    url=self.baseurl + "/" + endpoint,
                                    headers=self.headers,
                                    params=MergeDict(self.default_params, params),
                                    verify=self.ssl_verify
                                    )

        response_ = response.json()

        if response.status_code == 401:
            try:
                response_['message']
            except TypeError:
                raise exceptions.MissingPermission(response_)
            else:
                raise exceptions.MissingPermission(response_['message'])
        elif response.status_code == 422:
            errors = []
            for key in response_['errors']:
                errors.append(RemoveFromString(["<strong>", "</strong>"],
                                               response_['errors'][key][0])
                              + " (" + key + ")")
            raise exceptions.InvalidData(response_['message'] +
                                         "\n" +
                                         "\n".join(errors))
        # elif response.status_code != 200 and response.status_code != 201:
        #    raise exceptions.Error(response_['message'])
        elif response.status_code == 429:
            # We hit the maximum requests
             raise exceptions.TooManyAttempts(response_['message'])
        return response_

    def ping(self):
        data = self.call(endpoint="ping")
        return data
    
    """_summary_
    """    
    def set_order_id(self, order_id):
        self.order_id = order_id
