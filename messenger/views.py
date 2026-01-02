from rest_framework.viewsets import ModelViewSet

from messenger.models import Message
from messenger.serializers import MessageSerializer, MessageDetailSerializer


class MessageViewSet(ModelViewSet):
    def get_serializer_class(self):
        match self.action:
            case "retrieve":
                return MessageDetailSerializer

        return MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()

        match self.action:
            case "retrieve":
                queryset = queryset.select_related("user")

        return queryset
