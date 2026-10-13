def ticketGenerator():
    #discount Showed
    print('-------Welcome to eTrain Tickets-------')
    print('Type\t Discount')
    print('Student\t 7%')
    print('Child\t 25%')
    print('Type\t 15%')
    print('---------------------------------------')
    #Fair showed
    print('---------------Fare---------------')
    print(f"{'Rajshahi':<12}{'Chittagong':<12}{'Sylhet':<12}")
    print(f"{'495':<12}{'515':<12}{'500':<12}")
    print('----------------------------------')
    #variables
    Sfare=500
    Cfare=515
    Rfare=495
    passenger=[]
    ptype=[]
    totalFare=float()
    childCount=0
    seniorCount=0
    studentCount=0
    generalCount=0
    discount=float(0)
    #Input taken
    destination=input(' Enter Destination from Dhaka - Sylhet/Rajshahi/Chittagong: ')
    ticketCount=int(input('How many tickets you want to buy?\n= '))
    passenger=[]
    ptype=[]
    for i in range(ticketCount):
        name=input(f"Passnger {i+1} Name: ")
        type=input(f"Passnger {i+1} Type: ")
        passenger.append(name)
        ptype.append(type)      
    #Calculation starts
    # Rajshahi   
    if destination=='Rajshahi':
        totalFare=ticketCount*Rfare
        for i in range(ticketCount):
            if ptype[i]=='Child':
                discount+=Rfare*0.25
                childCount+=1
            elif ptype[i]=='Student':
                discount+=Rfare*0.07
                studentCount+=1
            elif ptype[i]=='Senior':
                discount+=Rfare*0.15
                seniorCount+=1
            else:
                generalCount+=1
    #Chittagong            
    elif destination=='Chittagong':
        totalFare=ticketCount*Cfare
        for i in range(ticketCount):
            if ptype[i]=='Child':
                discount+=Cfare*0.25
                childCount+=1
            elif ptype[i]=='Student':
                discount+=Cfare*0.07
                studentCount+=1
            elif ptype[i]=='Senior':
                discount+=Cfare*0.15
                seniorCount+=1
            else:
                generalCount+=1    
    #Sylhet    
    elif destination=='Sylhet':
        totalFare=ticketCount*Sfare
        for i in range(ticketCount):
            if ptype[i]=='Child':
                discount+=Sfare*0.25
                childCount+=1
            elif ptype[i]=='Student':
                discount+=Sfare*0.07
                studentCount+=1
            elif ptype[i]=='Senior':
                discount+=Sfare*0.15
                seniorCount+=1
            else:
                generalCount+=1
    else:
        print('Invalid Input')
        return
    #Statement
    print('############Ticket Details#############')
    if destination=='Rajshahi':
        print(f"{'Type':<20}{'count':<15}{'Fare':<15}")
        print(f"{'General':<20}{generalCount:<15}{generalCount*Rfare:<15}")
        print(f"{'Child':<20}{childCount:<15}{childCount*Rfare:<15}")
        print(f"{'Student':<20}{studentCount:<15}{studentCount*Rfare:<15}")
        print(f"{'Senior Citizen':<20}{seniorCount:<15}{seniorCount*Rfare:<15}")
        print('---------------------------------------')
        print("Subtotal=",totalFare,"\t Discount=",discount)
        netPrice=totalFare-discount
        print('Net Price(After Discount)=', netPrice)
    if destination=='Chittagong':
        print(f"{'Type':<20}{'count':<15}{'Fare':<15}")
        print(f"{'General':<20}{generalCount:<15}{generalCount*Cfare:<15}")
        print(f"{'Child':<20}{childCount:<15}{childCount*Cfare:<15}")
        print(f"{'Student':<20}{studentCount:<15}{studentCount*Cfare:<15}")
        print(f"{'Senior Citizen':<20}{seniorCount:<15}{seniorCount*Cfare:<15}")
        print('---------------------------------------')
        print("Subtotal=",totalFare,"\t Discount=",discount)
        netPrice=totalFare-discount
        print('Net Price(After Discount)=', netPrice)
    if destination=='Sylhet':
        print(f"{'Type':<20}{'count':<15}{'Fare':<15}")
        print(f"{'General':<20}{generalCount:<15}{generalCount*Sfare:<15}")
        print(f"{'Child':<20}{childCount:<15}{childCount*Sfare:<15}")
        print(f"{'Student':<20}{studentCount:<15}{studentCount*Sfare:<15}")
        print(f"{'Senior Citizen':<20}{seniorCount:<15}{seniorCount*Sfare:<15}")
        print('----------------------------------------')
        print("Subtotal=",totalFare,"\t Discount=",discount)
        netPrice=totalFare-discount
        print('Net Price(After Discount)=', netPrice)
    print("#### Thanks for using eTicket ####")

ticketGenerator()
       



    

