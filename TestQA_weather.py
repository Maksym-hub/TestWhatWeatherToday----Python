weather_today =  int(input("Введите целое число: "))

if weather_today in range (-50,0):
    print("It’s super cold today. Be sure you dressed well!")
elif weather_today in range (0,11):
    print("It’s windy outside, but we are sure you will enjoy your day!")
elif weather_today in range (11,31):
    print("It’s time for outdoor walking!")
elif weather_today in range (31,41):
    print("It's so hot outside!")
elif weather_today in range (41,51):
    print("Welcome to hell!")
else :
    print("Please re-check results in 5 mins")