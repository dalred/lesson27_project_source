import json

from django.shortcuts import render
from django.http import JsonResponse

from django.views.generic.base import View
from django.views.generic import DetailView

from categories.models import Categories
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def categories(request) -> JsonResponse:
    if request.method == "GET":
        categories_list = Categories.objects.all()
        response = []
        for category in categories_list:
            response.append(
                {
                    "id": category.id,
                    "name": category.name
                }
            )
        return JsonResponse(response, safe=False, status=200)

    elif request.method == "POST":
        category_data = json.loads(request.body)

        category = Categories()
        category.name = category_data.get("name")

        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, status=200)


# Почему то решили что на корневые должно быть FBV
# @method_decorator(csrf_exempt, name='dispatch')
# class CategoryView(View):
#     def post(self, request):
#         category_data = json.loads(request.body)
#
#         category = Categories.objects.create(
#             name=category_data.get("name"),
#         )
#
#         return JsonResponse({
#             "id": category.id,
#             "name": category.name
#             })

class CategoryDetailView(DetailView):
    model = Categories

    def get(self, request, *args, **kwargs) -> JsonResponse:
        try:
            category = self.get_object()
        except Categories.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })
