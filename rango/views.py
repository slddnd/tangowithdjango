from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

# Create your views here.
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    context_dict = {'boldmessage': "This is about rango, if we still havent finished, yell!"}
    return render(request, 'rango/about.html', context_dict)


def category(request, category_name_slug):

    # create a context dictionary which we can pass to the template rendering engine
    context_dict = {}
    print(category_name_slug)
    print()

    try:
        # attempts to find a cat-name slug with the same name, otherwise DNE exception
        category = Category.objects.get(slug=category_name_slug)
        context_dict[category] = category.name

        # now we need all the pages which are in our category
        pages = Page.objects.filter(category=category)

        # adds our results to context dict as pages
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        pass

    print(context_dict)

    return render(request, 'rango/category.html', context_dict)