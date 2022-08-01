from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from . import models
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.urls import reverse


def home(request, filter_category=""):
    if request.user.is_authenticated is False:
        return redirect(reverse('login', args=()))
    # return HttpResponse("<h1>HOME PAGE</h1>")

    categories = models.ReceiptCategory.objects.all()

    # receipts = models.Receipt.objects.all().filter(category=models.ReceiptCategory.objects.get(title="Борщ"))
    receipts = models.Receipt.objects.all()
    print(receipts)
    print(type(receipts))
    print(receipts[0].description)
    print(type(receipts[0].description))
    print("\n\n**********\n\n")

    if filter_category:
        receipts1 = []
        for receipt in receipts:
            print(receipt.category.all())
            print(type(receipt.category.all()))
            all_receipts = receipt.category.all()

            # all1 = []
            # for x in all_receipts:
            #     all1.append(x.title)
            all = [x.title for x in all_receipts]  # затолкали в новый массив все заголовки категорий

            if filter_category in all:  # если в массиве есть такая "строка"
                receipts1.append(receipt)
        receipts = receipts1

    context = {"receipts": receipts, "categories": categories}
    return render(request, 'app_teacher/pages/home.html', context)


def receipt(request, receipt_id):
    if request.user.is_authenticated is False:
        return redirect(reverse('login', args=()))
    # return HttpResponse("<h1>HOME PAGE</h1>")
    receipts = models.Receipt.objects.all().filter
    receipt = get_object_or_404(models.Receipt, pk=receipt_id)
    context = {"receipt": receipt}
    return render(request, 'app_teacher/pages/receipt.html', context)


def login(request):
    print(request.user.is_authenticated)

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(f'username: {username}')
        print(f'password: {password}')

        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
            print("success")
        else:
            print("fail")
    context = {}
    return render(request, 'app_teacher/pages/login.html', context)


def register(request):
    print(request.user.is_authenticated)

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(f'username: {username}')
        print(f'password: {password}')

        user = authenticate(username=username, password=password)
        if user:
            django_login(request, user)
            print("success")
        else:
            print("fail")
    context = {}
    return render(request, 'app_teacher/pages/register.html', context)


@csrf_exempt
def api_result(request):
    if request.method == "POST":
        data = request.POST.get("value", "данные не пришли!")
        print(data)
        return HttpResponse(data)
    recept_queryset = models.Receipt.objects.all()
    recept_list = []
    for i in recept_queryset:
        recept_list.append(i.title)
    return JsonResponse({"recepts": recept_list})


def api_result_id(request, recept_id):
    try:
        recept_queryset = models.Receipt.objects.get(id=recept_id)
        return JsonResponse({"recepts": recept_queryset.title})
    except Exception as error:
        return JsonResponse({"recepts": "Recept not have"})
