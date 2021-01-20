import phonenumbers
from phonenumbers import geocoder,carrier
given_No=input("Enter the no:")
number=phonenumbers.parse(given_No)
print(carrier.name_for_number(number,"en"))
print(geocoder.description_for_number(number,"en"))
if phonenumbers.is_valid_number(number)==False:
    print("Not a valid number")
Y=phonenumbers.format_number(number,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
print(Y)
