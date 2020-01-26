# dsproject
Resizable Arrays in Optimal Space & Time.

# Instructions

1. Following functions has 2 classes 'ResizableArray1' and 'ResizableArray2'.

# a. Grow:
     This function will increase the array at nth position and will create new array twice the size of previous one once array      is full.
# b. Shrink:
     This function will remove the element at the nth position.
# c. GrowForward:
     This is a coonditional function will add element to the arrayat uth position, where u = u+1 and n = n+1, and the capacity of array becomes equal to or not equals to u then it will call the function 'GrowBackward'.
# d. ShrinkForward:
     This is another conditional funtion which will deleteelement from the array at the uth position, where u = u-1 and n = n-1.
# e. GrowBackward:
     This conditional function add element to the arrayat ith position, where i = l-1 and n = n+1, when value of l becomes zero it will automatically call GrowForward fuction.
# f. ShrinkBackward:
     The function will delete element from the array present at lth position, where l = l+1 and n = n-1
     
# Driver Code Instructions
1. clone the code here:
   https://github.com/MuhammadAnwarBadat/dsproject.git
   
2. The test code is as under:
  a. Passing element in function 'a.Grow(n)' will add element inside the array.
  b. Passing parameter in function 'a.Shrink()' will delete last element from the array.
  c. Passing element in function 'a.GrowForward' will decrease 'l' and increase 'n' i.e the value of u will be increased in an array.
  d. Passing parameter in function 'a.ShrinkBackward()' will increase 'l' and decrease 'n' i.e delete the value of n in an array.
  e. Passing element in function'a.GrowBackward(n)' will increase 'n' i.e add element to the array and decrease 'l'
  f. Passing parameter in function 'a.ShrinkForward(n)' will delete an element from the array and will return the deleted    element.
# Sample Test Code:
def Test1():
    a = ResizableArray1()
    a.Grow(n)
    a.Shrink()
    a.Print()
    a.len()
    print(a.len())

def Test2():
    a = ResizableArray2()
    a.GrowForward(n)
    a.ShrinkBackward()
    a.GrowBackward(n)
    a.ShrinkForward()
    a.Print()
    print(a.capacity, a.l, a.u, a.n)
Test1()
Test2()

