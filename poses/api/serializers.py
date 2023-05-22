from rest_framework.serializers import ModelSerializer

from poses.models import Pose

class PoseSerializer(ModelSerializer):
    class Meta:

        model = Pose
        fields = '__all__'
