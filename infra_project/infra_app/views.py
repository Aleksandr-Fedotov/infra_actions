from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'У меня получилось! ... '
        'не с первого раза... '
        'далеко не с первого... '
        'но, получилось!'
    )


def second_page(request):
    return HttpResponse('А это вторая страница!')
