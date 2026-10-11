name=input("Enter your name:")
marks=[]

for x in range(5):
    mark=float(input((f'Enter course {x+1} marks= ')))
    marks.append(mark)

total=float(0)
passed=0
for x in marks:
    total+=x
    if(x>=50):
        passed+=1

average=total/5
maximum=max(marks)
minimum=min(marks)
print('-----------------------')
print('Name:',name,'\nTotal mark:',total,'\nHighest mark:',maximum,'\nAverage mark:',average,'\nLowest mark:', minimum)
print('Number of passed courses= ',passed)

if average>=80:
    print('Excellent')

elif average>=70:
    print('Good')

elif average>=60:
    print('Satisfactory')

elif average>=50:
    print('Pass')

else:
    print('Needs Improvement')

print('-----------------------')

print('End of performance evaluation')