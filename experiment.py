# file: experiment 
# kan later weer weggegooid worden 


# creeer een letterreeks 

# initialisaties
reeks = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
toonladder = list()
start_index = 0 
grondtoon = 'a' # dit wordt een parameter

if grondtoon != 'a':
  start = grondtoon  
  for i in range(0,7,1):
      if start == reeks[i]:
         # debug 
         # print(reeks[i])
         toonladder.append(reeks[i])
         start_index = i
      else:
         if  start_index != 0 :
             #  debug  
             # print(reeks[i])
             toonladder.append(reeks[i])
         i=i+1    
  huidige_lengte = len(toonladder)
else:
  huidige_lengte = 0  

# nog aanvullen na g en beginnen bij a

#debug
#print(toonladder)
#print('lengte ', huidige_lengte )
aantal_ontbrekende = 8 - huidige_lengte
#print('aantal_ontbrekende ', aantal_ontbrekende )

toevoeging = reeks[0:aantal_ontbrekende]
#debug
#print(toevoeging)

toonladder = toonladder+toevoeging

if grondtoon == 'a':
   toonladder.append(grondtoon)

# return toonladder

# debug
print(toonladder)

# test waarden start in ['a', 'b', 'f', 'g']
# gaat goed voor b, f en g
