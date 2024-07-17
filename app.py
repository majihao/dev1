import threading
import time
m={'a':1,"b":2}
for name,ite in m.items():
    print(name,ite)
print("All threads have been started.")
a=[]
c=[0,1,2,3,4]
d=[7,8]
a.extend(d)
print(a)