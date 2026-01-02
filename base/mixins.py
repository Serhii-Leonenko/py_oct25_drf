class ActionSerializerMixin:
    action_serializers = {}

    def get_serializer_class(self):
        if serializer := self.action_serializers.get(self.action):
            return serializer
        return super().get_serializer_class()
