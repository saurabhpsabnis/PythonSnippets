'''
Graph Class and methods
@auther Saurabh P Sabnis 
'''

class math_Ops:
    "Different mathematical operations from simple to complex"
    
    def __init__(self,para1=0,para2=0):
        self.para1 = para1
        self.para2 = para2
        
    def factorial(self,n):
        "Factorial using recursion"
        if n <= 1:
            return 1;
        else:
            return n*self.factorial(n-1)

if __name__ == '__main__': 
    
    mathOps = math_Ops()
    print " Factorial of" + str(12) + "is" + str(mathOps.factorial(12))
    