from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from somewhere import handle_uploader_file

def upload_file(request):
    if request.method == 'post':
        form = UploadFileForm(request.POST, s.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html', {'form':form}) 
