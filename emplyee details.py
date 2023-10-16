class dinesh:
   def __init__(self,cyn,id,firstname,lastname,Salary,loc,address,dob,adhaar):
     self.cyn=cyn
     self.id=id
     self.fn=firstname
     self.ln=lastname
     self.salary=Salary
     self.loc=loc
     self.address=address
     self.dob=dob
     self.adhaar=adhaar
     self.cynid=self.cyn+self.id

class tcs(dinesh):
  def salary_format(self):
    self.salary=f"{float(self.salary):.2f}"
  def show(self):
    print("my id is",self.cynid,"\nmy name",self.fn,self.ln,"\nmy salary is",self.salary,"\nmy loc",self.loc,"\naddress",self.address,"\nmy dob",self.dob,"\nadhaar",self.adhaar)

class hcl(dinesh):
  def salary_format(self):
    self.salary=(self.salary)-(0.1*self.salary)
  def update(self,gender):
    self.loc=gender
  def update (self,bloodgroup):
    self.addresss=bloodgroup
  def update (self,doj):
    self.dob=doj
  def show(self):
    print("my id is",self.cynid,"\nfirst name",self.fn,"\nsecondname",self.ln,"\nmy salary is",self.salary,"\nmy gender",self.loc,"\nmy bloodgroup",self.address,"\nmy doj",self.dob,"\nadhaar",self.adhaar)

class infy(dinesh):
    def salary_format(self):
      self.salary=(12*self.salary)
    def update (self,exp):
      self.loc=exp
    def update(self,mobile):
     self.address=mobile
    def update(self,address):
      self.dob=address
    def show(self):
      print("my id is",self.cynid,"\nfirst name name",self.fn,self.ln,"\nmy salary is",self.salary,"\nmy exp",self.loc,"\nmy mobile",self.address,"\nmy address",self.dob,"\nadhaar",self.adhaar)

d=tcs("tcs","23","dineshkumar","r",30000,"tnager","chennai","15/1/1993","none")
e=hcl("hcl","34","dinesh","kumar",30000,"male","o+","10/2/2023","none")
f=infy("infy","55","thennarasu","r",30000,"2 years",978811,"1/3 chennsai","1121 3343 3455")

d.salary_format()
d.show()
print()
e.salary_format()
e.show()
print()
f.salary_format()
f.show()
