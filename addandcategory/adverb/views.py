import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import DetailView
from django.views.generic.base import View

from adverb.models import Ads
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def advertisements(request) -> JsonResponse:
    if request.method == "GET":
        adv_list = Ads.objects.all()
        response = []
        for adv in adv_list:
            response.append(
                {
                    "id": adv.id,
                    "author": adv.author,
                    "price": adv.price,
                    "description": adv.price,
                    "address": adv.address,
                    "is_published": adv.is_published,
                }
            )
        return JsonResponse(response, safe=False)

    elif request.method == "POST":
        adv_data = json.loads(request.body)

        adv = Ads()
        adv.name = adv_data.get("name")

        adv.save()

        return JsonResponse({
            "id": adv.id,
            "author": adv.author,
            "price": adv.price,
            "description": adv.price,
            "address": adv.address,
            "is_published": adv.is_published,
        }, status=200)


class AdvEntityView(View):
    def get(self, request, pk) -> JsonResponse:
        adv = get_object_or_404(Ads, id=pk)

        return JsonResponse({
            "id": adv.id,
            "author": adv.author,
            "price": adv.price,
            "description": adv.price,
            "address": adv.address,
            "is_published": adv.is_published,
        }, status=200)
