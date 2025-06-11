unit=int(input("Enter unit: "))
if unit>0 and unit<=100:
    a=5
    bill=unit*a
    print("Your bill is: ",bill)
    
elif unit>100 and unit<=200:
       b=unit-100
       bf=b*8
       bb=100*5
       print("Your bill is: ",bf+bb)

elif unit>200:
      aa=(100*5)+(100*8)
      c=unit-200
      cc=c*10
      print("Your bill is: ",cc+aa)
else :
      print("invalid inpit!")

#-------------------------------------------Electricity bill










    # print(bill)




