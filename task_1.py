# task_1
def show(lst,target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                return [i,j]
lst = [2,7,11,15]
target = 18
res = show(lst,target)
print(res)

# task_2
def disp(s):
    lst1 = []
    dct1 = {')':'(','}':'{',']':'['}
    for i in s:
        if i in dct1.values():
            lst1.append(i)
        elif i in dct1.keys():
            if not lst1 or lst1[-1] != dct1[i]:
                return False
            lst1.pop()
        else:
            return True
    return len(lst1) == 0
input = "[](){}"
res1 = disp(input)
print(res1)

# task_3
def dispshow(lst2,k):
    dct2 = {}
    for i in lst2:
        dct2[i] = dct2.get(i, 0)+1
    c = sorted(dct2.items(),key=lambda x: x[1], reverse=True)
    res = [c[i][0] for i in range(k)]
    return res
lst2 = [1,1,1,2,2,3]
k = 3
print(dispshow(lst2,k))
