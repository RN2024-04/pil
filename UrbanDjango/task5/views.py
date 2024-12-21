from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from task5.models import News,Buyer



# Create your views here.
# def test(request):
#     Buyers=Buyer.objects.all()
#     context={
#         'Buyers':Buyers,
#     }
#     for i in Buyer.username:
#         users = [{i}]
#     return render(request, 'fifth_task/registration_page.html', context)

# users = [user]
def post_list(request):
    posts = News.objects.all().order_by('-id')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj= paginator.get_page(page_number)

    return render(request, 'news.html', {page_obj:page_obj})


# def post_list_view(request):
#     per_page = request.GET.get('per_page') or 2
#     posts = News.objects.all().order_by('-id') or per_page
#     paginator = Paginator(posts, per_page)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#
#     context = {'posts': posts}
#     return render(request, 'news.html', context)


def sign_up_by_html(request):
        info = {
        }
        users= Buyer.objects.values_list('username', flat=True)
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = int(request.POST.get('age'))

            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
                return HttpResponse('Пароли не совпадают')
            elif age < 18:
                info['error'] = "Вы должны быть старше 18"
                return HttpResponse('Вы должны быть старше 18')
            elif username in users:
                info['error'] = "Пользователь уже существует"
                return HttpResponse('Пользователь уже существует')
            else:
                info['welcome_message'] = f"Приветствуем, {username}!"
                Buyer.objects.create(username=username, password=password, repeat_password=repeat_password, age=age)

            return HttpResponse(f"Приветствуем, {username}!")


        return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_django(request):
    info = {}
    users = Buyer.objects.values_list('username', flat=True)
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
                return HttpResponse('Пароли не совпадают')
            elif age < 18:
                info['error'] = "Вы должны быть старше 18"
                return HttpResponse('Вы должны быть старше 18')
            elif username in users:
                info['error'] = "Пользователь уже существует"
                return HttpResponse('Пользователь уже существует')
            else:
                info['welcome_message'] = f"Приветствуем, {username}!"
                Buyer.objects.create(username=username, password=password, repeat_password=repeat_password, age=age)
            return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegister()
        info['message'] = form

    return render(request, 'fifth_task/registration_page.html', info)