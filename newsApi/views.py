from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from .models import NewsModel
from .newsScrap import fetch_news
from .serializer import NewsSerializers


@api_view(['GET'])
def get_skySportNews(request):
    if request.method == 'GET':
        news = NewsModel.objects.all()
        serializer = NewsSerializers(news, many=True)

        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'POST'])
def fetch_data(request):
    fetch_news()

    return Response(status=status.HTTP_206_PARTIAL_CONTENT)
