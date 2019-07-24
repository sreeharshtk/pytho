import itertools 
import functools 
  
lis = [ 1, 3, 4, 10, 4 ] 
  
print ("The summation of list using  is :",end="") 
print (list(itertools.accumulate(lis,lambda x,y : x+y))) 
  
print ("The summation of list using reduce is :",end="") 
print (functools.reduce(lambda x,y:x+y,lis)) 
