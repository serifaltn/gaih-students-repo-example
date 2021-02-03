seriflist = [0,1,2,3,4,5,6,7,8,9]
temp=seriflist[0:5]
seriflist[0:5]=seriflist[5:10]
seriflist[5:10]=temp
print(seriflist)

