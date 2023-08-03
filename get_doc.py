from datetime import datetime, timedelta
from elasticsearch import Elasticsearch


def summarize_elasticsearch_data():
    # Elasticsearch connection settings
    es_host = 'localhost'
    es_port = 9200


    es = Elasticsearch(hosts=[{'host': es_host, 'port': es_port}])


    index_name = 'test'

    # Calculate the time range for the past one hour
    end_time = datetime.now()
    start_time = end_time - timedelta(minutes=5)

    # Elasticsearch query to retrieve data within the time range
    query = {
        "query": {
            "bool": {
                "must": [
                    {
                        "range": {
                            "timestamp": {
                                "gte": start_time.strftime('%Y-%m-%dT%H:%M:%S'),
                                "lt": end_time.strftime('%Y-%m-%dT%H:%M:%S')
                            }
                        }
                    }
                ],
                "must_not": [
                    {
                        "regexp": {
                            "status_code": "2.*"
                        }
                    }
                ]
            }
        },
        "aggs": {
            "average_price": {
                "avg": {
                    "field": "price"
                }
            }
        }
    }
    query2 = {

    }
    # Search for documents and calculate average price using aggregation
    response = es.search(index=index_name, body=query, size=0)

    # Process the response to retrieve the average price
    average_price = response['aggregations']['average_price']['value']

    # Print the average price
    print(average_price)



# Call the function to summarize Elasticsearch data
summarize_elasticsearch_data()
