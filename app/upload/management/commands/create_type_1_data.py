import string
import random

from django.core.management import BaseCommand
from django.utils.timezone import datetime
from upload.models import Type1


def random_name(size=10, chars=string.ascii_uppercase):
    return "".join(random.choice(chars) for _ in range(size))


def random_email():
    pre = "".join(random.choice(string.ascii_lowercase + string.digits))
    domain = random.choice(["com", "org", "in", "on", "out"])
    return f"{pre}@{domain}"


def id_generator(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def generate_date():
    return datetime(random.randint(2000, 2020), month=random.randint(1, 12), day=random.randint(1, 28),
                    hour=random.randint(0, 23), minute=random.randint(0, 59))


class Command(BaseCommand):
    def handle(self, *args, **options):
        count = 0
        while count < 21:
            obj = Type1.objects.create(
                    Booking_ID=id_generator(),
                    No_of_nights=random.randint(1, 10),
                    Check_In=generate_date(),
                    Check_Out=generate_date(),
                    Room=random.randint(1, 2),
                    Night=random.randint(1, 10),
                    Hotel_Sell_Price=random.randint(1000, 50000),
                    Extra_Adult_Child_Charge=random.randint(0, 500),
                    Hotel_Gross_Price=random.randint(100, 500),
                    MMT_Commission=random.randint(100, 200),
                    GST_18_Including_IGST_or_SGST_CGST=random.randint(100, 500),
                    MMT_to_Pay_Hotel_A_B=random.randint(100, 500),
                    GST_on_hotel_accommodation_charges_by_Ecommerce_Operator=random.randint(100, 500),
                    Primary_Guest=random_name(),
                    E_mail=random_email(),
                    Contact_No="".join([random.choice(string.digits) for _ in range(10)]),
                    Room_Category=random.choice(["Garden View", "Lake View", "River Front"]),
                    Meal_Plan=random.choice(["Breakfast", "Lunch", "Dinner"])
                )
            self.stdout.write(self.style.SUCCESS(obj.Booking_ID + " created."))
            count += 1
