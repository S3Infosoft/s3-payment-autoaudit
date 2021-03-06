from operator import itemgetter

from django.db.models.functions import datetime

from rest_framework.generics import ListAPIView
from .serializers import Type1Serializers, Type8Serializers, Type9Serializers, CustomerNameSerializer
from ..models import Type1, Type8, Type9, Customer


class CustomerNameListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerNameSerializer


class Type1ListAPIView(ListAPIView):
    serializer_class = Type1Serializers

    def get_queryset(self):
        year1, month1, day1 = itemgetter(
            "year1", "month1", "day1"
        )(self.kwargs)
        year2, month2, day2 = itemgetter(
            "year2", "month2", "day2"
        )(self.kwargs)

        date1 = datetime.datetime(int(year1), int(month1), int(day1))
        date2 = datetime.datetime(int(year2), int(month2), int(day2))

        qs = Type1.objects.filter(
            Check_In__range=(date1, date2)
        )

        return qs


class Type8ListAPIView(ListAPIView):
    """ListView to display the data"""
    serializer_class = Type8Serializers
    queryset = Type8.objects.all()


class Type9ListAPIView(ListAPIView):
    """ListView to display the data"""
    serializer_class = Type9Serializers
    queryset = Type9.objects.all()
