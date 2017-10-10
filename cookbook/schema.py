import graphene
import cookbook.ingredients.schema

class Query(cookbook.ingredients.schema.Query, graphe.ObjectType):
    pass

schema = graphene.Schema(query=Query)
