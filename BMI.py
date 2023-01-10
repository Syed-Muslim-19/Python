height=input("ENTER THE HEIGHT in METERs : ")
weight=input("ENTER THE WEIGHT(KGs) : ")
bmi=float(weight)/(float(height)*float(height))
BMI=str(bmi)
print("The BMI Value is : "+BMI)
if bmi<18.49:
    print("UNDERWEIGHT")
elif 24.99>bmi and bmi>18.49:
       print("NORMAL WEIGHT")
elif 29.99>bmi and bmi>25:
       print("OVERWEIGHT")
else:
    print("OBESE")