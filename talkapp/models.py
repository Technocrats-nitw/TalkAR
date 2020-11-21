from django.db import models
from django.db.models import fields
from django.forms import ModelForm

# Create your models here.
class DataForm(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    contact = models.CharField(max_length=10)
    
class DataIn(ModelForm):
    class Meta:
        model = DataForm
        fields = ['name','message','contact']