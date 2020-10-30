from django.core import serializers
from exam.models import que
json_serializer = serializers.get_serializer("json")()
ex = json_serializer.serialize(que.objects.all().order_by('id')[:5], ensure_ascii=False)