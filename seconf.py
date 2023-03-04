import phonenumbers
from phonenumbers import timezone,geocoder,carrier
num = input("Enter your mno with +__")
phone = phonenumbers.parse(num)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print(phone,time,car,reg)
