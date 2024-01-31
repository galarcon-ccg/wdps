import os
from sgqlc.endpoint.http import HTTPEndpoint
from .queries import query_GetAllGenes

class WSGenes():
    """docstring for WSGenes."""
    def __init__(self):
        gql_url = os.environ.get("GQL_SERVICE")
        self.gql_service = HTTPEndpoint(gql_url)
    
    def getAll_genes(self):
        try:
            data = self.gql_service(query_GetAllGenes)
            return data
        except Exception as e:
            print("error to query getAllGenes:",e)
            return {"error": "query getAllGenes"}