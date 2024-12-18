from .forms import ImageForm, DocumentForm
from .models import ImageModel, DocumentModel
from django.shortcuts import render, redirect

# Create your views here.


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = ImageForm()
    return render(request, 'image_upload.html', {'form': form})


def image_list_view(request):
    images = ImageModel.objects.all()
    return render(request, 'image_list.html', {'images': images})


def upload_file_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = DocumentForm()
    return render(request, 'file_upload.html', {'form': form})


def file_list_view(request):
    files = DocumentModel.objects.all()
    return render(request, 'file_list.html', {'files': files})
