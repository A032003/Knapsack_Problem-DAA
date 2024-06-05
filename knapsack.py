import copy
opw = [[1,9,2],[2,15,3],[3,12,5],[4,4,4],[5,6,3],[6,16,6],[7,8,3]]
capacity_list = []
temp_opw = copy.deepcopy(opw)
capacity = 18

def remove_from_list(temp,ele):
    temp_L = []
    for i in temp:
        if i != ele:
            temp_L.append(i)
    return temp_L

# _________________________________________________________________________

# sort for p

max_p = []
temp_set = []
current = -1000
curr_w = 1000
for j in range(0,len(opw)):
    current = -1000
    curr_w = 1000
    for i in temp_opw:
        if current == i[1]:
            if curr_w > i[2]:
                current = i[1]
                temp_set = i
                curr_w = i[2]
        elif i[1]>current:
            current = i[1]
            temp_set = i
            curr_w = i[2]
    max_p.append(temp_set)
    temp_opw = remove_from_list(temp_opw,temp_set)
print()
print('_______________________________________________________________________________________________________________________')
print('Sorted Max Profit Order : [Object,Profit,Weight]        Capacity = ',capacity)

print(max_p)

# max profit
profit = 0
remaining_capacity = capacity
for i in max_p:
    if remaining_capacity>i[2]:
        remaining_capacity-=i[2]
        profit+=i[1]
    elif remaining_capacity<i[2]:
        profit+=(float(remaining_capacity)/float(i[2]))*i[1]
        remaining_capacity = 0

print('Maximum Profit : ',round(profit,3))
print()


# _________________________________________________________________________


temp_opw = copy.deepcopy(opw)
capacity = 18

# sort for w
max_w = []
temp_set = []
current = 1000
curr_p = -1000
for j in range(0,len(opw)):
    current = 1000
    curr_p = -1000
    for i in temp_opw:
        if current == i[2]:
            if i[1]>curr_p:
                current = i[2]
                temp_set = i
                curr_p = i[1]
        elif i[2]<current:
            current = i[2]
            temp_set = i
            curr_p = i[1]
    max_w.append(temp_set)
    temp_opw = remove_from_list(temp_opw,temp_set)

print('_______________________________________________________________________________________________________________________')
print('Sorted Min Weight Order : [Object,Profit,Weight]        Capacity = ',capacity)
print(max_w)

# min weight

profit = 0
remaining_capacity = capacity
for i in max_w:
    if remaining_capacity>i[2]:
        remaining_capacity-=i[2]
        profit+=i[1]
    elif remaining_capacity<i[2]:
        profit+=(float(remaining_capacity)/float(i[2]))*i[1]
        remaining_capacity = 0

print('Maximum Profit : ',round(profit,3))
print()

# _________________________________________________________________________

# profit per weight

temp_opw = copy.deepcopy(opw)
capacity = 18

for i in temp_opw:
    i.append(round(float(i[1]/float(i[2])),3))

# sort for ppw
max_ppw = []
temp_set = []
current = -1000
curr_p = -1000
for j in range(0,len(opw)):
    current = -1000
    curr_p = -1000
    for i in temp_opw:
        if current == i[3]:
            if i[1]>curr_p:
                current = i[3]
                temp_set = i
                curr_p = i[1]
        elif i[3]>current:
            current = i[3]
            temp_set = i
            curr_p = i[1]
    max_ppw.append(temp_set)
    temp_opw = remove_from_list(temp_opw,temp_set)

print('_______________________________________________________________________________________________________________________')
print('Sorted Max Ratio Order : [Object,Profit,Weight,Ratio]   Capacity = ',capacity)
print(max_ppw)

# max ppw profit
profit = 0
remaining_capacity = capacity
for i in max_ppw:
    if remaining_capacity>i[2]:
        remaining_capacity-=i[2]
        profit+=i[1]
    elif remaining_capacity<i[2]:
        profit+=(float(remaining_capacity)/float(i[2]))*i[1]
        remaining_capacity = 0

print('Maximum Profit : ',round(profit,3))
print()
# print('_______________________________________________________________________________________________________________________')