name=str (input("Enter your name\n: "))
basic=int(input("Enter your salary\n= "))
allowance=int(input("Enter allowance\n= "))
gross_sal=basic+allowance
print(name)

print("Gross Salary= ",gross_sal)

if(gross_sal<30):
    print("0% tax ",gross_sal)

elif(gross_sal>=30000 and gross_sal<=50000):
    print("5% tax ",gross_sal-(gross_sal*0.05))

elif(gross_sal>50000 and gross_sal<=80000):
    print("5% tax ",gross_sal-(gross_sal*0.10))

else:
    print("tax 15% ",gross_sal-(gross_sal*0.15))
