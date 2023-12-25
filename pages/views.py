from django.shortcuts import render

from pages.models import ScrollModel, GallaryModel, MenuModel


def home_page_view(request):
    scrolls = ScrollModel.objects.all().order_by('-id')[:5]
    gallary = GallaryModel.objects.all().order_by('-id')
    menus = MenuModel.objects.all().order_by('id')
    context = {
        'scrolls': scrolls,
        'gallaries': gallary,
        'menus': menus
    }
    return render(request, "index.html", context)