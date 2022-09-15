'''class Point:
    def __init__(self,y):
        self.y=y
        print("init called")

    def __add__(self,obj):
        print("add called")
        y=self.y+obj.y
        return Point(y)

p1=Point(10)
p2=Point(20)
print((p1+p2).y)
'''

d={1:"Vinit",2:"Amit",3:"Savan",4:"Dhruv",5:"Naresh",6:"Sonalisha",7:"Mayank",8:"Krupa",9:"Ronak"}

print(d)
print(d[3])
#print(d["Amit"])
d1=d.copy()
print(d1)
print(d.get(5))
print(d.items())
print(list(d.keys()))
print(d.values())
print(d.pop(3))
print(d)
print(d.popitem())
print(d)
d2={10:"Mehul",11:"Harsh",12:"Ravi",13:"Rehan"}
d.update(d2)
print(d)

for i in d:
    print(i," : ",d[i])
