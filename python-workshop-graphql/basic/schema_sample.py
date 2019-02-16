import graphene
from graphene.types import Scalar
from graphql.language import ast
import datetime


class Workshop(graphene.Enum):
    PYTHON = 2.7
    GO = 1.11
    JAVA = 1.8

    @property
    def description(self):
        if self == Workshop.PYTHON:
            return 'programming language that lets you work quickly and integrate systems more effectivel'
        return 'Other language'


class DateTime(Scalar):
    '''DateTime Scalar Description'''

    @staticmethod
    def serialize(dt):
        return dt.isoformat()

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return datetime.datetime.strptime(
                node.value, "%Y-%m-%dT%H:%M:%S.%f")

    @staticmethod
    def parse_value(value):
        return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")


class Person(graphene.ObjectType):
    name = graphene.String()




class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="stranger"))
    time = DateTime


    def resolve_hello(self, info, argument):
        return 'Hello ' + argument

    def resolve_code(self, info, argument):
        return "CODE " + argument

    def resolve_date(self, info, argument):
        return "CODE " + argument

schema = graphene.Schema(query=Query)
graphene.Field(graphene.String, to=graphene.String())

# result = schema.execute('{ hello }')
# print(result.data['hello']) # "Hello stranger"
#
# # or passing the argument in the query
# result = schema.execute('{ hello (argument: "graph") }')
# print(result.data['hello']) # "Hello graph"


schema = graphene.Schema(query=Query)
result = schema.execute('{ DateTime }')
print(result.data['PYTHON'])  # "Hello stranger"
