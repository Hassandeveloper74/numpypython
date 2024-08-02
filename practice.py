import numpy as np
# numpy is bassically used for numerical value and functions e.g : means, mode etc

# list [1,24,45,6,78] anywhere stored where memory is free
# array [1 2 3 4 5 6] occupied fixed memory cell means store in consective memory 



# l1=[1,2,45,6,7,8]
# l2=[1,23,4,5,6,7]         simple list show concatination value 
# print(l1+l2)

# ARRAY CREATION

# a=np.array([2,4,5])
# b=np.array([[4,6,7],[9,9,7]])
# print(b)
# print(a+b)
# print(a*b)

# slicing


# a=np.array([2,4,5,46,7,8])
# print(a[0:3])
# print(a[3:])
# print(a[:3])

# a=np.array([[2,4,5,46,7,8],[2,3,5,6,8,9]])
# print(a[0:4,0:4])

# a=np.array([[2,4,5,46,7,8],[2,3,5,6,8,9]])
# print(a[1,0:2])             //for multiple array indexing

# a=np.array([[2,4,5,46,7,8],[2,3,5,6,8,9]])
# print(np.shape(a))               //for shape how much row and colomn

# a=np.array([[2,4,5,46,7,8],[2,3,5,6,8,9]])
# print(np.ndim(a))                      //for dimendion of array 2d 3d etc

# a=np.array([[2,4,5,46,7,8],[2,3,5,6,8,9]])
# print(np.size(a))                       //total element  in array

# a=np.array([[2,4,5,46,7,8],[2,3,5,6,8,9]])
# print(len(a))                            //number of  rows in array

# a=np.array([[2,4,5,46,7,8],[2,3,5,6,8,9]])
# print(a.astype(float))                     //for datatype convertion

# a=np.array([[2,4,5,46,7,8],[2,3,5,6,8,9]])
# b=np.array([[2,4,6,46,7,8],[7,5,5,6,8,9]])
#  print(a+b)                                    ///for multiplication and subtraction etc
# print(np.add(a,b))
# print(np.subtract(a,b))


# a=np.array([2,4,5,46,7,8])
# b=np.array([3])
# print(np.power(a,b))            for power function

# a=np.array([4,4,46,8])
# print(np.sqrt(a))                for square root

# a=np.array([2,4,5,46,7,8])
# b=np.array([2,4,6,46,7,8])           for concatenation
# print(np.concatenate([a,b]))


# a=np.array([[2,4,5,46,7,8],[2,3,5,6,7,8]])
# b=np.array([[2,4,6,46,7,8],[7,5,5,6,8,9]])
# print(np.concatenate([a,b],axis=0))           # with axis concatenation
# print(np.hstack([a,b]))        #  //horizontol concatenation

# a=np.array([[2,4,5,7,8],[2,4,5,6,4]])
# c=np.array_split(a,2)                  spliting array 2d or one d
# print(c)           

# a=np.array([[9,4,5,9,8],[2,3,5,6,7]])
# print(np.append(a,49))          for single array append 
# print(np.append(a,[1,4]))       for 2d ARRAY append at last

# print(np.insert(a,1,[3,4,3,4,5], axis=0))         //for imserting
# print(a)
# print(np.delete(a,9))    //deletion

# print(np.sort(a))             //for sorting

# s=np.where(a==9)               //searching
# print(s)

# ar=np.array([3,4,6,8,4])
# fa=[False,True,True,True,True]
# new=ar[fa]                                 for filtering and creating new array by old array
# print(new)

# ar=np.array([3,4,6,8,4])
# # fa=ar>2                                   also filter like this
# new=ar[fa]
# print(new)
# ar=np.array([3,4,6,8,4])

# print(np.mean(ar))               // mean value finding

ar=[3,86,7,45,4]
ab=[5,4,6,8,4]

price=np.array(ab)
q=np.array(ar)

print(price,"\n",q)
print()

c=np.cumprod([price,q],axis=0)
print(c[1].sum())



print
