import graphene
import graphql_jwt
from apps.users.schema import UserQuery, UserMutation
from apps.posts.schema import PostQuery, PostMutation

class Query(UserQuery, PostQuery, graphene.ObjectType):
    pass

class Mutation(UserMutation, PostMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
