from django.shortcuts import render, reverse, get_object_or_404
from cv.models import Personal, Image, MyInfo
from django.http import HttpResponse, Http404, HttpResponseRedirect
from cv.forms import ImageForm
# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    context = {'about':MyInfo.objects.all()}
    return render(request, 'about.html', context)

def skills(request):
    return render(request, 'skills.html')

def work(request):
    context = {'works':Image.objects.all()}
    return render(request, 'mywork.html',context)

def cv(request):
    context = {'file':Personal.objects.all()}
    return render(request, 'cv.html', context)

def download(request, path):
    file_path= os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,"rb") as fh:
            response= HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']= 'inline;filename='+os.path.basename(file_path)
            return response
    raise Http404


def work_form(request):
    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("personal:work"))
    context = {"form": form}
    return render(request, "work_form.html", context)
