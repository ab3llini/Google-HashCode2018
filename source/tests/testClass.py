from source.greedy.element import Element
from source.greedy.elementList import ElementList
from source.greedy.greedy import greedy


class RealElement(Element):

    def clone(self):
        return RealElement(self.value)

    def __init__(self, num):
        self.value = num

    def get_value(self):
        return self.value


class RealElementList(ElementList):

    def clone(self):
        return RealElementList([element.clone() for element in self.get_elements()])

    def __init__(self, elements):
        super(RealElementList, self).__init__(elements)

    def ind(self, element):
        return True


a = RealElementList([RealElement(7), RealElement(2), RealElement(1), RealElement(0), RealElement(10), RealElement(4)])
b = a.clone()
a.sort()
a.insert(5)
for elem in a.get_elements():
    print(elem.get_value())
for elem in b.get_elements():
    print(elem.get_value())

print("******")

for elem in b:
    print(elem.get_value())

print("******")

b.sort()
for elem in b:
    print(elem.get_value())

print("******")

sol = greedy(b)
for elem in sol:
    print(elem.get_value())

