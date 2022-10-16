from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from .models import (
    Post,
    Rate,
)
from .serializers import PostSerializer


# Create your views here.

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rate_view(request, pk):
    try:
        rate_value = float(request.GET.get('rate'))
    except ValueError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    if not 0 <= rate_value <= 5:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    post = Post.objects.get(pk=pk)
    rating, created = Rate.objects.update_or_create(post=post, user=request.user, defaults={'rating': rate_value})
    return redirect('post_detail', pk=pk)
