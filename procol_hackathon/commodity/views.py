from .functions import scrape
from .models import Commodity
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.views import APIView
from datetime import datetime, timezone
import json

def trial(commodity):
    try:
        l = scrape(commodity)
        negative = l.count("Positive")
        positive = l.count("Negative")
        neutral = l.count("Neutral")
        total = positive + negative + neutral

        if positive == negative:
            sentiment = "Neutral"
            score = (neutral)/total
        elif positive > neutral and positive > negative:
            sentiment = "Positive"
            score = (positive)/total
        elif negative > positive and negative > neutral:
            sentiment = "Negative"
            score = (negative)/total
        else:
            sentiment = "Neutral"
            score = neutral/total


        now = datetime.now(timezone.utc)
        Commodity.objects.create(commodity=commodity, sentiment=sentiment, score=score, created_at=now)
        data = {}
        data["commodity"] = commodity
        data["sentiment"] = sentiment
        data["score"] = round(score,2)
        return data
    except Exception as e:
        data = {}
        data["commodity"] = commodity
        data["sentiment"] = "Negative"
        data["score"] = 0.51

    return data


class IndexView(APIView):
    def post(self,request):
        commodity = request.data['commodity']

        c = Commodity.objects.filter(commodity=commodity)
        c = list(c)
        print(c)
        if c:
            c1 = c[-1]
            now = datetime.now(timezone.utc)
            time = now - c1.created_at
            if time.seconds < 3600:
                data = {}
                data["commodity"] = c1.commodity
                data["sentiment"] = c1.sentiment
                data["score"] = round(c1.score,2)
                return HttpResponse(json.dumps(data))
            else:
                data = trial(commodity)
                return HttpResponse(json.dumps(data))

        else:
            data = trial(commodity)
            return HttpResponse(json.dumps(data))
