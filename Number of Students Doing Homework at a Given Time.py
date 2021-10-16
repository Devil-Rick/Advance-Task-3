"""
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, 
return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.
"""
startTime = list(map(int, input('Start Time = ').split(',')))
endTime = list(map(int, input('End Tine = ').split(',')))
queryTime = int(input('Query Time = '))
c = 0
for i in range(len(startTime)):
    if queryTime <= endTime[i] and queryTime >= startTime[i]:
        c += 1
print(c)
