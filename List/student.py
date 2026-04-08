
scores = []
total = 0.0

n = int(input("Enter number of student that you want to add: "))

for i in range(1,n+1):
    corrent_score = float(input(f"Enter the sore {i} : "))
    scores.append(corrent_score)
    
    total = total + corrent_score

# total = sum(scores)
avg = total/len(scores)

if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade ='C'
elif avg >= 60:
    grade = 'D'
elif avg >= 50:
    grade = 'E'
else :
    grade = "F"
    
print(f"The total score is: {total}")
print(f"The average is: {avg}")
print(f"The Grade is: {grade}")