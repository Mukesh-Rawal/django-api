from django.http import HttpResponse,JsonResponse

def home(request):
    print('Page requested')

    fruits_list = [
        'banana',
        'apple',
        'guava',
    ]

    return JsonResponse(fruits_list, safe=False)