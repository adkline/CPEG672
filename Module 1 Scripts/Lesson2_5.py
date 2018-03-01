import time, hashlib

n = input("Enter Password ")

def hashing_func(n):
    r = 3
    starttime = time.clock()
    salt = "somesalt"
    x = hashlib.sha256(n + salt).digest()

    while (r>1):
      y = hashlib.sha256(x + n + salt).digest()
      x = y
      r = r-1
    
    endtime = time.clock()

    return endtime-starttime, r, y                                                                    

            
