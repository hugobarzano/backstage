# from graphene import relay
# import graphene as graphene
# from schema import Ninja
# from schema  import create_ninja
#
# import graphene as graphene
# from graphene.relay import Node
#
# class AddNinja(relay.ClientIDMutation):
#
#     '''mutation M {
# 	    addNinja(input:{name:"new"}) {
# 	    ninja{
#             name
#         }
# 	    }
#     }'''
#
#     class Input:
#         name = graphene.String(required=True)
#
#         ninja = graphene.Field(Ninja)
#
#     @classmethod
#     def mutate_and_get_payload(cls, root, info, **input):
#         ninja = create_ninja(input["name"])
#         return AddNinja(ninja=ninja)