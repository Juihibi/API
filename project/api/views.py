from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost
from .serializers import BlogPostSerializer


# Create your views here.

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.object.all().delete()
        return Response(status = status.HTTP_284_NO_CONTENT)




class BlogPostRetieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'
      
class BlogPostList(APIView):
    def get(self, request, format = None):
        # Get the title from the query parameters (if nonem default to empty string)
        title = request.query_params.get('title', '')

        if title:
            # Filter the queryset based on the title
            blog_post = BlogPost.object.filter(title__icontains = title)
        else:
            # If no title is provided, return all the blog post
            blog_post = BlogPost.object.all()


        serializer = BlogPostSerializer(blog_post, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
