list=[350,22,45,350,350,720,880,954,58]
listtri=[]

def max_list(lst) :
    lenth = len(lst)
    if(lenth == 1):
        return lst[0]
    max_s1 = max_list(lst[0: (lenth//2)])
    max_s2 = max_list(lst[(lenth//2) : lenth])
    if(max_s1 > max_s2):
        return max_s1
    return max_s2

def tri_max_list(list):
    if len(list)==1:
        listtri.append(list[0])
        return listtri
    listtri.append(max_list(list))
    list.remove(max_list(list))
    tri_max_list(list)
    return listtri

print(tri_max_list(list))

