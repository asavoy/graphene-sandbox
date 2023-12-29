from graphene import Field, List, ObjectType, Schema, String

from graphene_sandbox.data import get_friends, get_person


class Person(ObjectType):
    name = String(required=True)
    best_friend = Field(lambda: Person)
    friends = List(lambda: Person)

    @staticmethod
    def resolve_best_friend(parent, info):
        return get_person(parent["best_friend_name"])

    @staticmethod
    def resolve_friends(parent, info):
        return get_friends(parent["name"])


class RootQuery(ObjectType):
    me = Field(Person)

    @staticmethod
    def resolve_me(parent, info):
        return get_person("Me")


schema = Schema(query=RootQuery)
