import random 
 while (True): 
   a=random.randint(5,99) 
   b=random.randint(5,99) 
   if(a>30 and b>70): 
       print("high temperature and humidity    of:",a,b,"%","alarm is on") 
   elif(a<30 and b<70): 
       print("normal temperature and humidity of:",a,b,"%","alarm is off") 
       break