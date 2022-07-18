#Write a Python Program to Create a Lap Timer

import time
  
starttime = time.time()
endtime = starttime
lapnumber = 1
value = ""
  
print("Press ENTER for each lap \nType QUIT to stop.")
  
while value.lower() != "quit":
              
    value = input()
  
    laptime = round((time.time() - endtime), 2)
  
    totaltime = round((time.time() - starttime), 2)
  
    print("Lap Number: "+str(lapnumber))
    print("Total Time: "+str(totaltime))
    print("Lap Time: "+str(laptime))
            
    print("*"*20)
  
    endtime = time.time()
    lapnumber+= 1
  
print("stopped")