
from django import forms
from .models import Pose

class PoseForm(forms.ModelForm):
    class Meta:
        model = Pose
        fields = '__all__'
        exclude = ['posted_by', 'updated_at', 'created_at']
        enctype = "multipart/form-data"
