import random
test_list=[0,1,2,4,5,2,5,88]

# the times of the function calls itself is less than N(the size of a).
def max(a,l,r):
    # a is a list
    # l is the start index of a
    # r is the end inde of a
    m = (l+r)//2
    if l==r:
        return a[l]
    u = max(a,l,m)
    v = max(a,m+1,r)
    if u>v:
        return u
    else:
        return v

start = 0
end = len(test_list)-1
print(max(test_list,start,end))
