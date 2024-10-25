# apps/users/mutations.py
import graphene
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required
from .types import UserType

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        bio = graphene.String(required=False)

    def mutate(self, info, username, email, password, bio=None):
        try:
            User = get_user_model()
            # First create the user without bio
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            # Then set the bio if provided
            if bio:
                user.bio = bio
                user.save()
                
            return CreateUser(success=True, user=user)
        except Exception as e:
            return CreateUser(success=False, errors=[str(e)])

class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        bio = graphene.String()

    @login_required
    def mutate(self, info, bio=None):
        try:
            user = info.context.user
            if bio:
                user.bio = bio
            user.save()
            return UpdateUser(success=True, user=user)
        except Exception as e:
            return UpdateUser(success=False, errors=[str(e)])