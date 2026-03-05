#Classes are templates for a type of object
class Point():
    def __init__(self, input1, input2):
    # Magic method: self references the object that we are dealing with
         self.x = input1
         self.y = input2
p = Point(2, 8)
print(p.x)
print(p.y)
