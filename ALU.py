#  python  C:\example.py

#Funtions bollock
# OP    No CARRY    CARRY           FUNCTION
# 1     A          A + 1            Transfer    / Increment 
# 2     A + B      (A + B) + 1      Add         / Add with carry 
# 3     A + !B      A + !B + 1      Subtract    / A plus 1's complement of B
# 4     A - 1       A               Decrement   / Transfer
# 5     A LSL       A  LSL + 1      Logical Shift Left  / Logical Shift Left with borrow (.. may work?)
# 6     A SRL       A  SRL + 1      Logical Shift Right / Logical Shift Right with borrow (.. may work?)
# 7     XOR         
# 8     OR          
# 9     !XOR
# 10    AND

#Variables

a = 16
b = 16
x = range(b)

def printblock(): #Weighting. E = 8, N = 4, Z = 2, C = 1
    if n == i:
        E = 8
    else:
        E = 0
        
    if (OP) == 0:
        Z = 2
    else:
        Z = 0 
        
    if (OP) < 0:
        N = 4
    else:
        N = 0  

    if (OP) > 15:
        C = 1
    else:
        C = 0            
    
    if (OP) < 16 and (OP) > 0:
        print hex(E + N + Z + C)[2:],                #Neg 0, Zero 0, Carry 0         
        print hex(OP)[2:],
    elif (OP) == 0:
        print hex(E + N + Z + C)[2:],                #Neg 0 Zero 1 Carry 0        
        print (0), 
    elif (OP) < 0:
        print hex(E + N + Z + C)[2:],                #Neg 1 Zero 0 Carry 0         
        print hex(OP+16)[2:],        
    elif (OP) > 15:
        print hex(E + N + Z + C)[2:],                #Neg 0 Zero 0 Carry 1      
        print hex(OP-16)[2:],    

def inversion(a):        #I'm so sorry for anyone reading this. I couldn't think of a better way. I know there must be.
    if a == 15:
        b = 0
    if a == 14:
        b = 1
    if a == 13:
        b = 2
    if a == 12:
        b = 3
    if a == 11:
        b = 4
    if a == 10:
        b = 5
    if a == 9:
        b = 6
    if a == 8:
        b = 7
    if a == 7:
        b = 8
    if a == 6:
        b = 9
    if a == 5:
        b = 10
    if a == 4:
        b = 11 
    if a == 3:
        b = 12
    if a == 2:
        b =13
    if a == 1:
        b = 14
    if a == 0:
        b = 15  
    return b



#print("A & A+1")
for n in x:                         #Op1  Pass through.
  for i in range(a):
    OP = i
    printblock()
  print(" "),
  
  for i in range(a):                #Op1 with carry.  (Increment)
    OP = i + 1
    printblock()
  print(" ")  

#print("A+B & (A+B)+1")
for n in x:                         #Op2  A + B
  for i in range(a):
    OP = (i+n)
    printblock()
  print(" "),
  
  for i in range(a):                #Op2 with carry. (A + B) + 1
    OP = (i+n) + 1
    printblock()
  print(" ")
  
#print("A + !B      A + !B + 1      Subtract    / A plus 1's complement of B")
for n in x:                         #Op3  A + !B
  for i in range(a):
    OP = i + inversion(n)
    printblock()
  print(" "),
  
  for i in range(a):                #Op3 with carry. (A + B) + 1
    OP = (i + inversion(n)) + 1
    printblock()
  print(" ")
  
#print("A - 1       A               Decrement   / Transfer")
for n in x:                         #Op4  -A
  for i in range(a):
    OP = (i -1)
    printblock()
  print(" "),
  
  for i in range(a):                #Op4 With Carry A Transfer 
    OP = i
    printblock()
  print(" ")
    
#print("A LSL       A  LSL + 1         Logical Shift Left  / Logical Shift Left with borrow (.. may work?)")
for n in x:                         #Op5 
  for i in range(a):
    OP = i * 2 
    printblock()
  print(" "),
  
  for i in range(a):                #Op5 With Carry 
    OP = (i * 2) + 1
    printblock()
  print(" ")

#print("A SRL       A  SRL + 1         Logical Shift Right / Logical Shift Right with borrow (.. may work?)")
for n in x:                         #Op6 
  for i in range(a):
    OP = int(i / 2) 
    printblock()
  print(" "),
  
  for i in range(a):                #Op6 With Carry 
    OP = int((i+1) / 2)
    printblock()
  print(" ")
  
#print("XOR")
for n in x:                         #Op7   
  for i in range(a):
    OP = i ^ n 
    printblock()
  print(" "),
  
  for i in range(a):                #nop
    OP = i
    printblock()
  print(" ")
  
#print("OR")
for n in x:                         #Op8   
  for i in range(a):
    OP = i or n 
    printblock()
  print(" "),
  
  for i in range(a):                #nop
    OP = i
    printblock()
  print(" ")
  
#print("!XOR")
for n in x:                         #Op9
  for i in range(a):
    OP = inversion(i ^ n) 
    printblock()
  print(" "),
  
  for i in range(a):                #nop
    OP = i
    printblock()
  print(" ")
  
#print("!XOR")
for n in x:                         #Op10  
  for i in range(a):
    OP = i & n 
    printblock()
  print(" "),
  
  for i in range(a):                #nop
    OP = i
    printblock()
  print(" ")