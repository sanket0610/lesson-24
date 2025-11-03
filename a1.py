set1={1,5,3,6,2,4,5,7,7}
print(set1)
set2={"sashuel","hippuappu",6,7,9,6,19,18}
print(set2)
set3=set("hippuappu")
print(type(set3))
set1.pop()
print(set1)
set1.remove(3)
print(set1)

set3={3,35,7,8,9,178}
u=set1.union(set3)
print("union=",u)

i=set1.intersection(set3)
print("INTERSECTION=",i)