
##stuff = list()
##stuff.append('python')
##stuff.append('chuck')
##stuff.sort()
##print (stuff[0])
##
##print(stuff.__getitem__(0))
##print(list.__getitem__(stuff,0))

##stuff = list()
##print(dir(stuff))

##class PartyAnimal:
##    x = 0
##
##    def party(self) :
##        self.x = self.x + 1
##        print('So far:',self.x)
##        
##an = PartyAnimal()
##an.party()
##an.party()
##an.party()
##PartyAnimal.party(an)

#### just having a little fun with type
##franz = list
##webster = dict
##
##print(type(franz))
##print(type(webster))

#### THIS IS party5.py
##class PartyAnimal:
##   x = 0
##   name = ''
##   def __init__(self, nam):
##     self.name = nam
##     print(self.name,'was constructed')
##
##   def party(self) :
##     self.x = self.x + 1
##     print(self.name,'party count',self.x)
##
##s = PartyAnimal('Sally')
##s.party()
##j = PartyAnimal('Jim')
##j.party()
##s.party()

## THIS IS INHERITANCE party6.py ================================
from party import PartyAnimal

class CricketFan(PartyAnimal):
   points = 0
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
