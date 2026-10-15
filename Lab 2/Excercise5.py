studentInfo={'Name':'Antor', 'Id':'25-62318-2', 'Department':'Data Science', 'CGPA':3.83}
for x, value in studentInfo.items():
    print(f'{x:<15}:{value}')

if studentInfo['CGPA'] >=2.50:
    print('Good Standing')
else:
    print('Academic Warning')    