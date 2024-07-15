import random
temp= []
for i in range(7):
    temp.append(random.randint(26,41))
    
print(temp)
day = ["sun","mon","tues","wedn","thrs","friday","saturday"]
count = 0

for i in range (7):
    if temp[i] % 2 == 0 :
      print(day[i])
      count+=1
      
print(count)      

highest_temp = 0
for i in range(7):
    if temp[i] > highest_temp:
        highest_temp = temp[i]
        high_day = day[i]
    
print(highest_temp)
print(high_day)


lowest_temp = 0
for i in range(7):
    if temp[i] < lowest_temp:
        lowest_temp = temp[i]
        low_day = day[i]
    
print(lowest_temp)
print(low_day)
 
