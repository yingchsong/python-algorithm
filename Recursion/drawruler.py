
def ruler(l,r,h):
    # l : start
    # r : end
    # h: the height of marker
    m=(l+r)/2
    if h>0 :
        ruler(l,m,h-1)
        print(m,h)
        ruler(m,r,h-1) # do not use m+1

ruler(0,10,3)
