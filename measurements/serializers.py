from django.db.models import fields
from rest_framework import serializers
from measurements.models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):

    screen = serializers.ImageField(max_length=None,
                                    use_url=True,
                                    allow_null=True,
                                    required=False
                                    )

    class Meta:
        model = Measurement
        fields = '__all__'
