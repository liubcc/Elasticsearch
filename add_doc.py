from datetime import datetime
import random
from elasticsearch import Elasticsearch
import time

es = Elasticsearch('http://localhost:9200/')

def generate_document():
    status_code =  random.choice(["200", "301", "404", "500"])
    price = round(random.uniform(0.01, 1000.0),2)
    current_time = datetime.now()

    document = {
        'status_code' : status_code,
        'price' : price,
        'timestamp' : current_time
    }
    return document

index_name = 'employees'
doc_type = 'doc'

while True:
    document = generate_document()
    es.index(index = index_name, doc_type = doc_type, body = document)
    time.sleep(5)




