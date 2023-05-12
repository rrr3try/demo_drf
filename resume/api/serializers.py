from rest_framework import serializers

from resume.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Resume
        fields = ('owner', 'status', 'grade', 'specialty', 'salary', 'education', 'experience', 'portfolio', 'title')
