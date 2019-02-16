from graphene.test import Client
from schema import GenerateSchema
from database import *
import json
import ast



def test_allNinjas():

    schema = GenerateSchema()
    client = Client(schema)
    executed = client.execute('''{
                                    allNinjas {
                                        edges {
                                            node {
                                                id,
                                                name
                                            }
                                        }
                                    }
                                }''')

    response = json.dumps(executed , indent=4)
    response_dic=ast.literal_eval(response)
    print "::: DEBUG NODES :::\n"+str(response_dic["data"]["allNinjas"]["edges"])
    assert response_dic["data"]["allNinjas"]["edges"][0]["node"]["name"] == "Akira"
    assert response_dic["data"]["allNinjas"]["edges"][1]["node"]["name"] == "Teckshuo"


if __name__ == '__main__':
    init_connection(TEST_DATABASE,HOST)
    remove_db(TEST_DATABASE,HOST)
    init_db()
    test_allNinjas()
