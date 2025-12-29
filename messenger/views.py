from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ViewSet

from messenger.models import Message, Tag
from messenger.serializers import MessageSerializer, TagSerializer


# @api_view(["GET", "POST"])
# def message_list(request: Request) -> Response:
#     if request.method == "GET":
#         messages = Message.objects.all()
#         serializer = MessageSerializer(messages, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == "POST":
#         serializer = MessageSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class MessageView(APIView):
#     def get(self, request: Request) -> Response:
#         messages = Message.objects.all()
#         serializer = MessageSerializer(messages, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request: Request) -> Response:
#         serializer = MessageSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class TagView(APIView):
#     def get(self, request: Request) -> Response:
#         tags = Tag.objects.all()
#         serializer = TagSerializer(tags, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request: Request) -> Response:
#         serializer = TagSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomGenericView(APIView):
    queryset = None
    serializer_class = None

    def get_queryset(self):
        assert self.queryset is not None, "queryset is required"

        return self.queryset.all()

    def get_serializer_class(self):
        assert self.serializer_class is not None, "serializer_class is required"

        return self.serializer_class


class ListMixin:
    def list(self, request: Request, *args, **kwargs):
        instances = self.get_queryset()
        serializer = self.get_serializer_class()(instances, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateMixin:
    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomListCreateView(ListMixin, CreateMixin, CustomGenericView):
    def get(self, request: Request) -> Response:
        return self.list(request=request)

    def post(self, request: Request) -> Response:
        return self.create(request=request)


class MessageView(CustomListCreateView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class TagView(CustomListCreateView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
