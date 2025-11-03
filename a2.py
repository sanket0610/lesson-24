import array as arr
a=arr.array('i',[1,2,3,4,3,2,1,1,3,3,3,3])
print(a)
print("Number of occurance for number 3:",str(a.count(2)))
a.reverse()
print("REVERSED array:",a)
a.append(6)
print("Append array:",a)