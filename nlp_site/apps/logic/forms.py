from django import forms

class TopicForm(forms.Form):
    topic = forms.CharField(label='Input twitter topic here: ', max_length=100)
