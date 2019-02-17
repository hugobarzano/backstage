from database import *
from flask import Flask
from flask_graphql import GraphQLView
from schema import *

app = Flask(__name__)
app.debug = True

default_query = '''
{
  allNinjas {
    edges {
      node {
        id,
        name
      }
    }
  }
}'''.strip()

schema=GenerateSchema()
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    init_connection(DEV_DATABASE,HOST)
    remove_db(DEV_DATABASE,HOST)
    init_db()
    app.run(host='0.0.0.0',port='8080')
