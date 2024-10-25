import graphene
from graphql_jwt.decorators import login_required
from .types import PostType
from .models import Post
from .mutations import CreatePost, UpdatePost

class PostQuery(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=graphene.ID(required=True))

    def resolve_posts(self, info):
        return Post.objects.select_related('author').all()

    def resolve_post(self, info, id):
        try:
            return Post.objects.select_related('author').get(id=id)
        except Post.DoesNotExist:
            return None

class PostMutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()