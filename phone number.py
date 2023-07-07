import phonenumbers
from phonenumbers import timezone,carrier,geocoder 
number=input("Enter your number with +977: ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
carr=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(carr)
print(reg)

