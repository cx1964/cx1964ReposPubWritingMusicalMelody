# file: experiment 
# kan later weer weggegooid worden 


# creeer een letterreeks 
reeks = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

toonladder = list()
start_index = 0
start = 'b'
for i in range(0,7,1):
    if start == reeks[i]:
       print(reeks[i])
       toonladder.append(reeks[i])
       start_index = i
    else:
       if  start_index != 0 :  
           print(reeks[i])
           toonladder.append(reeks[i])
       i=i+1    

# nog aanvullen na g en beginnen bij a

print(toonladder)
