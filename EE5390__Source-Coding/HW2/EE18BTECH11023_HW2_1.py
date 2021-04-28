import math

def prob(s):
  p =1
  for i in range(len(s)):
    if(s[i]=='a'):
      p = p*pa
    elif(s[i]=='b'):
      p = p*pb
    else:
      p = p*pc
  return p
print('for the random Sequence:  cbaaaaabcb')   #starting of Random Sequence 1
m = []      #For Seq
x ="cbaaaaabcb" 
pa = 0.3685424963
pb =0.3328804453
pc = 0.2985770584
for i in range(0,len(x)-1):
  t = prob(x[0:len(x)-i-1])
  m.append(t)
  print(t)
def G(s):
  if(s=='a'):
    return 0
  elif(s=='b'):
    return pa
  else:
    return pa+pb

n = []
for i in range(0,len(x)):
  if(x[i]=='a'):
    n.append(0)
    print(0)
  elif(x[i]=='b'):
    n.append(pa)
    print(pa)
  else:
    n.append(pa+pb)
    print(pa+pb)

l = 0
l = l+n[0]
th = 0
th = th+n[0]
for i in range(len(m)):
  th = th+m[i]*n[len(n)-1-i]
print(th+(prob(x)/2))
print(int(math.log(1/prob(x),2))+2)    #end of Random Sequence 1
print("")
print("")

print('for the Random Sequence :bbaaaabacb')  #starting of Random Sequence 2
m1 = []
x1 ="bbaaaabacb"
for i in range(0,len(x1)-1):
  t = prob(x1[0:len(x1)-i-1])
  m1.append(t)
  print(t)
def G(s):
  if(s=='a'):
    return 0
  elif(s=='b'):
    return pa
  else:
    return pa+pb

n1 = []
for i in range(0,len(x1)):
  if(x1[i]=='a'):
    n1.append(0)
    print(0)
  elif(x1[i]=='b'):
    n1.append(pa)
    print(pa)
  else:
    n1.append(pa+pb)
    print(pa+pb)

l1 = 0
l1 = l1+n1[0]
th1 = 0
th1 = th1+n1[0]
for i in range(len(m1)):
  th1 = th1+m1[i]*n1[len(n1)-1-i]
print(th1+(prob(x1)/2))
print(int(math.log(1/prob(x),2))+2)    #Enp of Random Sequence 2
