import ctypes 
  
class ResizableArray1(object):
    def __init__(self): 
        self.n = 0  
        self.capacity = 1 
        self.A = self.make_array(self.capacity)
        self.u = 0
        self.l = 0
          
    def len(self): 
        return self.n 
      
    def locate(self, k): 
        if not 0 <= k <self.n:  
            return IndexError('Index out of range!')         
        return self.A[k]  
          

    def resize(self, new_cap): 
        B = self.make_array(new_cap)  
          
        for k in range(self.n):  
            B[k] = self.A[k] 

        self.A = B  
        self.capacity = new_cap 
        
    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
    

    def Print(self):
        for i in range(self.n):
            print(self.A[i])
        #for k in range(self.n):
        #return(self.A)

    def Grow(self,element):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)
        self.A[self.n] = element
        self.n = self.n + 1

    def Shrink(self):
        a = self.A[self.n - 1]
        self.A[self.n-1] = None
        self.n = self.n-1
        if self.n * 4 == self.capacity:
            self.resize(self.capacity//2)
        return a

class ResizableArray2(object):
    def __init__(self):
        self.n = 0  
        self.capacity = 1  
        self.A = self.make_array(self.capacity)
        self.u = 0
        self.l = 0

    def resize(self, new_cap):
        B = self.make_array(new_cap)
        
        for k in range(self.n):  
            B[k] = self.A[self.l+k]

        self.A = B  
        self.capacity = new_cap  

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()

    def len(self):
        return self.n

    def GrowForward(self,element):
        if self.n == self.capacity:
            self.resize(2 * self.capacity)

        if self.u == self.capacity and self.n < self.capacity:
            self.GrowBackward(element)
        else:
            self.A[self.u] = element
            self.n = self.n + 1
            self.u = self.u + 1

    def ShrinkForward(self):
        if self.n == 0:
            print('Array is Empty')
        a = self.A[self.u - 1]
        self.A[self.u - 1] = None
        self.u = self.u - 1
        self.n = self.n - 1
        if self.n * 4 == self.capacity:
            self.resize(self.capacity // 2)
        return a

    def Read(self,i):
        if l <= i <= u:
            return self.A[i]
        else:
            return ('index out of range')

    def Write(self,i,x):
        if l <= i <= u:
            self.A[i] = x
        else:
            return ('index out of range')

    def GrowBackward(self,element):
        if self.n == self.capacity:
            self.resize(2*self.capacity)
        if self.l > 0:
            self.A[self.l-1] = element
            self.n = self.n + 1
            self.l = self.l-1
        if self.l == 0:
            self.GrowForward(element)



    def ShrinkBackward(self):
        if self.n == 0:
            print('Array is Empty')
        a = self.A[self.l]
        self.A[self.l] = None
        self.l = self.l + 1
        self.n = self.n - 1
        if self.n * 4 == self.capacity:
            self.resize(self.capacity // 2)
            self.l = 0
            self.u = self.n
        return a

    def Print(self):
        for i in range(self.l,self.u):
            print(self.A[i])

def Test1():
    a = ResizableArray1()
    a.Grow(2)
    a.Grow(3)
    a.Grow(4)
    a.Print()
    a.len()
    print(a.len())

def Test2():
    a = ResizableArray2()
    a.GrowForward(2)
    a.GrowForward(3)
    a.GrowForward(5)
    a.GrowForward(9)
    a.GrowForward(6)
    a.ShrinkBackward()
    a.ShrinkBackward()
    a.ShrinkBackward()
    a.GrowBackward(13)
    a.GrowBackward(14)
    a.GrowBackward(15)
    a.ShrinkForward()
    a.GrowBackward(15)
    a.ShrinkBackward()
    a.ShrinkBackward()
    a.GrowForward(123)
    a.GrowForward(124)
    a.GrowForward(125)
    a.GrowForward(126)
    a.GrowForward(127)
    a.GrowBackward(128)
    a.Print()
    print(a.capacity, a.l, a.u, a.n)

Test1()
Test2()
