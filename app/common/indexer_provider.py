from app.common.indexer_factory import ElasticFactory
from elasticsearch import Elasticsearch


class ElasticProvider(object):

    def __init__(self, index_name, doc_type):
        self.index_name = index_name
        self.doc_type = doc_type
        self.elastic_factory = ElasticFactory()
        self.instance = None

    def connection(self) -> Elasticsearch:
        if not self.instance:
            self.instance = self.elastic_factory.create()

        return self.instance

    def search(self, search_payload):
        return self.connection().search(body=search_payload, doc_type=self.doc_type, index=self.index_name)
