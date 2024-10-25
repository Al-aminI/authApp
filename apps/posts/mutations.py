import graphene
from graphql_jwt.decorators import login_required
from .types import PostType
from .models import Post

class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    @login_required
    def mutate(self, info, title, content):
        print(f"Authenticated user: {info.context.user}") 
        try:
            post = Post(
                title=title,
                content=content,
                author=info.context.user
            )
            post.save()
            return CreatePost(success=True, post=post)
        except Exception as e:
            return CreatePost(success=False, errors=[str(e)])

class UpdatePost(graphene.Mutation):
    post = graphene.Field(PostType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        content = graphene.String()

    @login_required
    def mutate(self, info, id, title=None, content=None):
        print(f"User: {info.context.user}")
        try:
            post = Post.objects.get(id=id, author=info.context.user)
            if title:
                post.title = title
            if content:
                post.content = content
            post.save()
            return UpdatePost(success=True, post=post)
        except Post.DoesNotExist:
            return UpdatePost(success=False, errors=["Post not found or not authorized"])
        except Exception as e:
            return UpdatePost(success=False, errors=[str(e)])
