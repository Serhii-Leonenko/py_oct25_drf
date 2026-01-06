from django.core.exceptions import ObjectDoesNotExist
from rest_framework.relations import SlugRelatedField


class CreatableSlugRelatedField(SlugRelatedField):
    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get(**{self.slug_field: data})
        except ObjectDoesNotExist:
            # self.fail('does_not_exist', slug_name=self.slug_field, value=smart_str(data))
            return queryset.create(**{self.slug_field: data})
        except (TypeError, ValueError):
            self.fail("invalid")
