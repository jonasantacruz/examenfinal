from django.shortcuts import render
from django.utils import timezone
from .models import Libro
from .forms import LibroForm

def post_list(request):
    libros = Libro.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'libro/post_list.html', {})

def libro_new(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('libro.views.post_detail')
    else:
        form = LibroForm()
    return render(request, 'libro/post_edit.html', {'form': form})
    #form = LibroForm()
    #return render(request, 'libro/post_edit.html', {'form': form})
# Create your views here.
