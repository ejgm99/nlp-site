from django.shortcuts import render
from django import forms

print("This is successfully imported")

def formHandler(request, template_path, FormClass, handler):
    if request.method =='POST':
        form = FormClass(request.POST)
        if form.is_valid():
            #if form is valid, we read contents and run our query
            j = handler(request)
            return render(request, template_path, {'form': form, 'emoji_json':j})
    else:
        form = FormClass();
    return render(request, template_path, {'form': form})
