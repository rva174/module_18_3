from django.shortcuts import render

def platform(request):
    title = "Главная страница"
    main = "Главная"
    shop = "Магазин"
    basket = "Корзина"
    context = {
        "title": title,
        "main": main,
        "shop": shop,
        "basket": basket,
    }
    return render(request, 'third_task/platform.html', context)

def games(request):
    games_list = {
        "Atomic Heart": "Купить",
        "Cyberpunk 2077": "Купить",
        "Pay Day 2": "Купить",
    }
    context = {
        "games": games_list,
    }
    return render(request, "third_task/games.html", context)

def cart(request):
    return render(request, "third_task/cart.html")
