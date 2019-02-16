import graphene as graphene
from graphene.relay import Node
from graphene import relay

from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models.ninjaModel import Ninja  as NinjaModel


def create_ninja(input):
    ninja = NinjaModel(name=input)
    ninja.save()
    return ninja


class Ninja(MongoengineObjectType):
    class Meta:
        model = NinjaModel
        interfaces = (Node,)


class AddNinja(relay.ClientIDMutation):
    '''mutation M {
	addNinja(input:{name:"mata ninjas"}) {
	  ninja{
      name
      enrolled
    }
	}
}'''

    class Input:
        name = graphene.String(required=True)

    ninja = graphene.Field(Ninja)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        ninja = create_ninja(input["name"])
        return AddNinja(ninja=ninja)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_ninjas = MongoengineConnectionField(Ninja)
    enrolled = graphene.Field(Ninja)


class Mutation(graphene.ObjectType):
    add_ninja = AddNinja.Field()


def GenerateSchema():
    return graphene.Schema(query=Query, types=[Ninja, AddNinja], mutation=Mutation)

# schema = graphene.Schema(query=Query,mutation=Mutation,types=[Ninja])
