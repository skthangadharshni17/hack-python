def common(lis1,lis2):
        newlis=[]
        for i in lis1:
                for j in lis2:
                        if(i==j):
                                newlis.append(i)
        print("Common elements:",newlis)
        for i in newlis:
                c1=lis1.count(i)
                c2=lis2.count(i)
        print(i,"occurs",c1,"times in list1")
        print(i,"occurs",c2,"times in list2")
lis1=[1,2,3,1,2,3]
lis2=[1,2,5,6]
common(lis1,lis2)