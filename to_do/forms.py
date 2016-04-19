from django import forms
from .models import Todo_List

class TodoForm(forms.ModelForm):
	class Meta:
		model=Todo_List
		fields=['title', 'description']