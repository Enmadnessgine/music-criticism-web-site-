from django.views.generic import DetailView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Release

def index(request):
    releases = Release.objects.all()
    columns = range(3)
    return render(request, 'mainapp/index.html', {'releases': releases, 'columns': columns})

class ReleaseDetailView(DetailView):
    model = Release
    template_name = 'mainapp/release_detail.html'
    context_object_name = 'release'
