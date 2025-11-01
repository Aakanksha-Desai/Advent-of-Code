import pandas as pd

txt = open('C:\\Users\\aakan\\OneDrive\\Documents\\Advent of Code\\input1.txt', 'r')
##Part 1
# nums = ['0','1','2','3','4','5','6','7','8','9']
# total = 0
# for line in txt:
#     firstFlag = False
#     lastFlag = False
#     # print(line)
#     rev = line[::-1]
#     for i in range(len(line)):
#         if line[i] in nums and firstFlag == False:
#             first = line[i]
#             firstFlag = True
        
    
#     for j in range(len(rev)):
#         if rev[j] in nums and lastFlag == False:
#             last = rev[j]
#             lastFlag = True
        
#     result = first + last
#     res = int(result)
#     total += res
# print(total)
            
##Part 2
total = 0
nums1 = ['0','1','2','3','4','5','6','7','8','9']
nums = ['zero','one','two','three','four','five','six','seven','eight','nine']
d = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
nums_rev = []

for num in nums:
    nums_rev.append(num[::-1])
# print(nums_rev)
for line in txt:
    firstFlag = False
    lastFlag = False
    last_isnum = False
    first_isnum = False
    rev = line[::-1]
    for i in range(len(line)):
        if line[i:i+3] in nums and firstFlag == False:
            first = line[i:i+3]
            firstFlag = True
        elif line[i:i+4] in nums and firstFlag == False:
            first = line[i:i+4]
            firstFlag = True
        elif line[i:i+5] in nums and firstFlag == False:
            first = line[i:i+5]
            firstFlag = True
        elif line[i] in nums1 and firstFlag == False:
            first = line[i]
            firstFlag = True
            first_isnum = True
    for j in range(len(rev)):
        if rev[j:j+3] in nums_rev and lastFlag == False:
            last = rev[j:j+3]
            lastFlag = True
        elif rev[j:j+4] in nums_rev and lastFlag == False:
            last = rev[j:j+4]
            lastFlag = True
        elif rev[j:j+5] in nums_rev and lastFlag == False:
            last = rev[j:j+5]
            lastFlag = True 
        elif rev[j] in nums1 and lastFlag == False:
            last = rev[j]
            lastFlag = True
            last_isnum = True
    print("first"+first)
    print("last"+last)
    if not first_isnum:
        first_num = d[first] 
    else:
        first_num = first    
    if not last_isnum:
        last = last[::-1]
        last_num = d[last]
    else:
        last_num = last
    result = first_num + last_num
    res = int(result)
    print("res="+str(res))
    total += res
print(total)
            


