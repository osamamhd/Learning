from django import forms
from .models import Course,Topic,Assignment,Answer
from django.contrib.auth import get_user_model,get_user


class CreateCourseForm(forms.ModelForm):
    instructor = forms.ModelChoiceField(get_user_model().objects.all(), widget=forms.Select(attrs={'class':'form-control form-control-user'}))
    class Meta:
        model = Course
        fields= '__all__'
        widgets={
            'course_code':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Course Code'}),
            'course_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Course name'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':'3','id':'summernote'}),
            'levels':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'level':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'session':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'semester':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'video':forms.Textarea(attrs={'class':'form-control form-control-user','required':'required','placeholder':'Embed A Course related Youtube or Vimeo video here','rows':'3','cols':'5'}),       
            'file':forms.FileInput(attrs={'class':'form-control form-control-user'}),
            }

        help_texts = {
            "file":"<p class='text-danger'>Note: *.pdf, *.doc, *.docx, *.(jpg,png,gif) are accepted</p>"
        }

class CourseUpdateForm(forms.ModelForm):
   
    class Meta:
        model = Course
        exclude = ['instructor','file']
        widgets={
            'course_code':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Course Code'}),
            'course_name':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Course name'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':'3','id':'summernote'}),
            'levels':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'level':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'session':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'semester':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'video':forms.Textarea(attrs={'class':'form-control form-control-user','required':'required','placeholder':'Embed A Course related Youtube or Vimeo video here','rows':'3','cols':'5'}),       
        }
    

class CreateTopicForm(forms.ModelForm):
    instructor = forms.ModelChoiceField(get_user_model().objects.all(), widget=forms.Select(attrs={'class':'form-control form-control-user'}))
    class Meta:
        model = Topic
        fields= '__all__'
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Title'}),
            'course':forms.Select(attrs={'class':'form-control form-control-user','placeholder':'Course name'}),
            'contents':forms.Textarea(attrs={'class':'form-control','rows':'3' ,'id':'summernote'}),
            'levels':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'video':forms.Textarea(attrs={'class':'form-control form-control-user','required':'required','placeholder':'Embed A Topic related Youtube or Vimeo video here','rows':'3','cols':'5'}),       
            'file':forms.FileInput(attrs={'class':'form-control form-control-user'})
        }

        help_texts = {
            "file":"<p class='text-danger'>Note: *.pdf, *.doc, *.docx, *.(jpg,png,gif) are accepted</p>"
        }
      

class TopicUpdateForm(forms.ModelForm):
     class Meta:
        model = Topic
        exclude = ['instructor']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Title'}),
            'course':forms.Select(attrs={'class':'form-control form-control-user','placeholder':'Course name'}),
            'contents':forms.Textarea(attrs={'class':'form-control','rows':'3','id':'summernote'}),
            'levels':forms.Select(attrs={'class':'form-control form-control-user','placeholder':''}),
            'video':forms.Textarea(attrs={'class':'form-control form-control-user','required':'required','placeholder':'Embed A Topic related Youtube or Vimeo video here','rows':'3','cols':'5'}),       
            'file':forms.FileInput(attrs={'class':'form-control form-control-user'})
        }

        help_texts = {
            "file":"<p class='text-danger'>Note: Only uploads new files if you wish to change from existing one</p>"
        }

class CreateAssignmentForm(forms.ModelForm):
    #level = forms.CharField(choices=Assignment.choice,widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Assignment
        fields = "__all__"
        widgets={
            'course':forms.TextInput(attrs={'class':'form-control','placeholder':'Course Title'}),
            'question':forms.Textarea(attrs={'class':'form-control','placeholder':'Course Question','rows':'4'}),
            'level':forms.Select(attrs={'class':'form-control','placeholder':'Course Question'}),
            'author':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'})
        }

class StudentAnswerForm (forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'
        widgets={
            'course':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'matric':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'question':forms.Textarea(attrs={'class':'form-control','readonly':'readonly','rows':'4'}),
            'level':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'answer':forms.FileInput(attrs={'class':'form-control','required':'required'}),
            'author':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'})

        }