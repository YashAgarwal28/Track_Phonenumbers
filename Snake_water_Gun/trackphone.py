# First Step is to import phonenumbers libiary from pip
import phonenumbers
# Second Step Is to import geocoder, Carrier and timezone from phonenumbers libiary
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

# Now lets take a varibale phone_number1
phone_number1 = phonenumbers.parse("+8613262388725")
# Lets Just Print Headline
print("\n Phone Numbers Location\n")
# Print Phone Number
print("\n Phone Number Is :-",phone_number1)
# Print geocoder location
print("\n Geocoder of Number is:-",geocoder.description_for_number(phone_number1, "en"))
# Print Carrier Provider Name
print("\n Carrier Provider Name :-",carrier.name_for_number(phone_number1,"en"))
# Print TimeZone Of Provided Number
print("\n TimeZone Is :-",timezone.time_zones_for_number(phone_number1))