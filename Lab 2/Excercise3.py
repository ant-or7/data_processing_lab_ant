temp=(45.6,41.4,45,46,42.5,41)
for x,value in enumerate(temp): 
    if x==0:
        print("-------Saturday's Temperature--------")
    elif x==3:
        print("---------Sunday's Temperature---------")
    print(value)

print('Highest Temperature:', max(temp))
print("Lowest Temperature:", min(temp))