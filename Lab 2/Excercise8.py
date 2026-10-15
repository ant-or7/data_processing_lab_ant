studentInfo=[ {"name": "Rahim", "department": "CSE", "marks": 85, "attendance": 92}, 
            {"name": "Karim", "department": "CSE", "marks": 48, "attendance": 76}, 
            {"name": "Sara", "department": "DS", "marks": 91, "attendance": 95}, 
            {"name": "Nadia", "department": "DS", "marks": 67, "attendance": 84}, 
            {"name": "Hasan", "department": "CSE", "marks": 73, "attendance": 78} ]

def calculateAvg(studentInfo):
    totalMarks=0
    for x in studentInfo:
        totalMarks+=x['marks']

    avg=totalMarks/len(studentInfo)
    return avg

def findHighest(studentInfo):
    highest=-1
    index=0
    for x, value in enumerate(studentInfo):
        if value['marks']>highest:
            highest=value['marks']
            index=x
    return studentInfo[index]['name'], highest

def attendence(studentInfo):
    count=0
    for x in studentInfo:
        if x["attendance"]<80:
            count+=1
    return count
name,mark=findHighest(studentInfo)
print('======================Summary===================')
print(f'{'Average marks of students':<40}:{calculateAvg(studentInfo)}')
print(f"{'Name of the student with highest mark':<40}:{name} Mark= {mark}")
print(f'{'Student count whom attendance below 80%':<40}:{attendence(studentInfo)}')
print('================================================')
