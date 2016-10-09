from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    print "title: " + title
    file = forms.FileFiled()
