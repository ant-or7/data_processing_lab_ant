def calculateGrades(marks):
    total=float(0)
 
    for x in marks:
        total+=x

    average=total/len(marks)

    if average>=80:
        return 'A'

    elif average>=70:
        return 'B'

    elif average>=60:
        return 'C'

    elif average>=50:
        return 'D'

    else:
        return 'F'

#marks=[48,56,89,45,78]
print(calculateGrades([48,56,89,45,78]))
