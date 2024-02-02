import os
from sgqlc.endpoint.http import HTTPEndpoint

class WS_connect():
    """class to connect to web services"""
    def __init__(self, ):
        try:
            self._gql_url = os.environ.get("GQL_SERVICE")
            self._gql_service = HTTPEndpoint(os.environ.get("GQL_SERVICE"))
            self._connected = True
        except Exception as e:
            print("ws connect error: ",e)
            self._connected = False
    
    def is_connected(self):
        return self.connected
    
    def get_gql_service(self):
        return self._gql_service
    
    def get_gql_url(self):
        return self._gql_url