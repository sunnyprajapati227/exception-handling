#This is my class object#
#this is also enpasultion#
class student:
	def __init__(self):
		self.name=input("enter name:")
		self.email=input("enter email:")

	def show(self):	
		print("name:",self.name)
		print("class:",self.email)

s1=student()
s1.show()

s2=student()
s2.show()		