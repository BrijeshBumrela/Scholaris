from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from Discussion_Forum.models import Post
from .serializers import PostSerializer, ResultSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

# Create your views here.

def get_mean(marks):
    mean = 0
    marks = [int(mark) for mark in marks]

    for mark in marks:
        mean += mark
    return mean/len(marks)


@api_view(['GET','POST'])
@csrf_exempt
def post_list(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data['author'])
            if User.objects.filter(username=serializer.validated_data['author']).exists():
                user = User.objects.get(username=serializer.validated_data['author'])
                serializer.validated_data['author'] = user
                serializer.save()

                return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



@csrf_exempt
def post_detail(request, id):

    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data)


@api_view(['POST'])
@csrf_exempt
def result(request):
    serializer = ResultSerializer(data=request.data, many=True)

    if serializer.is_valid():
        data_obj = []
        for data in serializer.validated_data:
            data_obj.append(dict(data))

        marks = []
        for data_obj_mark in data_obj:
            marks.append(data_obj_mark['marks'])

        mean = get_mean(marks)

        return Response(mean, status=201)
    return Response('error',status=400)
