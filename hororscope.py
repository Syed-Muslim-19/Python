date=int(input("Enter the Date of Birth : "))
month=int(input("Enter the Months number : "))
if (month == 1 and (date >= 20 and date <= 31))or (month == 2 and (date <= 18 and date >= 1)):
	print("Aquarius")
elif(month == 2 and (date >= 19 and date <= 31))or (month == 3 and (date <= 20 and date >= 1)):
	print("Pisces")
elif(month == 3 and (date >= 21 and date <= 31))or (month == 4 and (date <= 19 and date >= 1)):
	print("Aries")
elif(month == 4 and (date >= 20 and date <= 31))or (month == 5 and (date <= 20 and date >= 1)):
	print("Taurus")
elif(month == 5 and(date >= 21 and date <= 31))or (month == 6 and(date <= 20 and date >= 1)):
	print("Gemini")
elif(month == 6 and(date >= 21 and date <= 31))or (month == 7 and (date <= 22 and date >= 1)):
	print("Cancer")
elif(month == 7 and (date >= 23 and date <= 31))or (month == 8 and(date <= 22 and date >= 1)):
	print("Leo")
elif(month == 8 and (date >= 23 and date <= 31))or (month == 9 and (date <= 22 and date >= 1)):
	print("Virgo")
elif(month == 9 and (date >= 23 and date <= 31)) or (month == 10 and (date <= 22 and date >= 1)):
	print("Libra")
elif(month == 10 and (date >= 23 and date <= 31))or (month == 11 and (date <= 21 and date >= 1)):
	print("Scorpio")
elif(month == 11 and (date >= 22 and date <= 31)) or (month == 12 and (date <= 21 and date >= 1)):
	print("Sagittarius")
elif(month == 12 and (date >= 22 and date <= 31)) or (month == 1 and (date <= 19 and date >= 1)):
	print("Capricorn")