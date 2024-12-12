year = int(input("Greetings! What is your year of origin? "))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
    print ("That's totally the present!")
elif year >= 2020:
    print ("Far out, that's the future!!")
