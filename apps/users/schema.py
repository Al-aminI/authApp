# apps/users/schema.py
import graphene
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required
from .types import UserType
from .mutations import CreateUser, UpdateUser

class UserQuery(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    @login_required
    def resolve_me(self, info):
        return info.context.user

    @login_required
    def resolve_users(self, info):
        return get_user_model().objects.all()

class UserMutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
