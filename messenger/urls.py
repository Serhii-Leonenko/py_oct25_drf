from django.urls import path
from messenger.views import MessageView, TagView

app_name = "messenger"

urlpatterns = [
    path("messages/", MessageView.as_view(), name="message-list"),
    path("tags/", TagView.as_view(), name="tag-list")
]
