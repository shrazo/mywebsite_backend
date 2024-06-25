from rest_framework import serializers
from .models import * 
# from django_quill.drf.fields import QuillHtmlField, QuillPlainField

class AboutSerializer(serializers.ModelSerializer):
    # description = QuillHtmlField()

    class Meta:
        model = About
        fields = "__all__"

# class AboutSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = About 
#         fields = '__all__'

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link 
        fields = '__all__'

class ResearchSerializer(serializers.ModelSerializer):
    # description = QuillHtmlField()
    class Meta:
        model = Research 
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication 
        fields = '__all__'

class HighlightSerializer(serializers.ModelSerializer):
    # description = QuillHtmlField()
    class Meta:
        model = Highlight 
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience 
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education 
        fields = '__all__'