# Starting with Multiple inheritance 
class grandfather:
  def __init__(self,gname,gage,gjob):
    self.gname = gname
    self.gage = gage
    self.gjob = gjob

    print("My Grand Father name is " + self.gname + "his age is " + str(self.gage) + " and his job is " + self.gjob)

class grandmother:
  def __init__(self,gname,gage,gjob):
    self.gmname = gname
    self.gmage = gage
    self.gmjob = gjob

    print("My Grand Mother name is " + self.gmname + "her age is " + str(self.gmage) + " and her job is " + self.gmjob)
    
# Father class inherits from grandfather and grand mother. 
class father(grandfather,grandmother):
  def __init__(self,fname,fage,fjob, gname,gage,gjob, gmname,gmage,gmjob):
    self.fname = fname
    self.fage = fage
    self.fjob = fjob
    grandfather.__init__(self,gname,gage,gjob)
    grandmother.__init__(self,gmname,gmage,gmjob)

    print ("Father has a lot of work to do and his name is " + self.fname + " his age is " + str(self.fage) + " and he is a " + self.fjob  )
    
# Multi level inheritance where child inherits from father where father inherits from grand father and grand mother. 
class child(father):
  def __init__(self, cname, cage, fname, fage, fjob, gname, gage, gjob, gmname, gmage, gmjob):
    self.cname = cname
    self.cage = cage
    father.__init__(self,fname, fage,fjob,gname,gage,gjob,gmname,gmage,gmjob)

    print("the child always helps his father the child name is " + self.cname + " his age is " + str(self.cage) )


c1 = child(" ali" , 33 , "Atta mohammad " , 66 , "Dr" , "Bahadur " , 92 , "Teacher" , " Dadi " , 88 , "housewife")

