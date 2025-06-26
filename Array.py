# Array = [90,80,100,70,40,30]
Array1 = [10,20,30,40,50]
Answer = True
for i in range(len(Array1)-1):
    if Array1[i] <= Array1[i+1]:
        continue
    else:
        Answer = False
        break

print(Answer)
