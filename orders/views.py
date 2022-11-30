from django.shortcuts import render, redirect

# Create your views here.
def basket(request):
    test = [1, 2, 3, 4, 5]
    context = {
        "content": test,
    }
    return render(request, "orders/basket.html", context)


def info(request):
    context = {
        "content": "결제 정보 페이지",
    }
    return render(request, "orders/info.html", context)


def payment(request):
    context = {
        "content": "결제 페이지",
    }
    return render(request, "orders/payment.html", context)


def complete(request):
    context = {
        "content": "결제완료 페이지",
    }
    return render(request, "orders/complete.html", context)
