from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from task5.models import News,Buyer

# Create your views here.

# def index(request):
#     posts = News.objects.all().order_by('-id')
#     paginator = Paginator(posts, 3)
#     page_number=request.Get.get('page')
#     page_obj=paginator.get_page(page_number)
#     return render(request, 'news.html', {'page_obj':page_obj})


def platform_templates(request):
    game_dict = {'games': ["Cyperpunk 2077", "Mario", "Hitman"]}
    game_dict2 = {'games': ["Game of the year", "Old game", "Who kills Mark?"]}
    context = {
        'game_dict': game_dict,
        'game_dict2': game_dict2,

    }

    return render(request, 'fourth_task/platform.html', context)

def games_templates(request):
    game_dict = {'games': ["Cyperpunk 2077", "Mario", "Hitman"]}
    game_dict2 = {'games': ["Game of the year", "Old game", "Who kills Mark?"]}
    context = {
        'game_dict': game_dict,
        'game_dict2': game_dict2,

    }

    return render(request, 'fourth_task/games.html', context)

def cart_templates(request):
    return render(request, "fourth_task/cart.html")