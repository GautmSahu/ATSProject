from rest_framework import serializers
from .models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'  # include all fields of the model