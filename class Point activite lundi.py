
import math

class Point:
    nb = 0 
    def __init__(self, abs, ord):
        self.__abs = abs
        self.__ord = ord
        Point.nb += 1

    @property
    def abs(self):
        return self.__abs

    @abs.setter
    def abs(self, value):
        self.__abs = value

    @property
    def ord(self):
        return self.__ord

    @ord.setter
    def ord(self, value):
        self.__ord = value

    def __str__(self):
        return f"Nombre:{Point.nb}\nabs = {self.__abs}\nord = {self.__ord}"

    def __eq__(self, other):
        return self.__abs == other.__abs and self.__ord == other.__ord

    def calculer_distance(self, p):
        return math.sqrt(math.pow((self.__abs - p.__abs), 2) + math.pow((self.__ord - p.__ord), 2))

    def calculer_milieu(self, p):
        x_milieu = (self.__abs + p.__abs) / 2
        y_milieu = (self.__ord + p.__ord) / 2
        return Point(x_milieu, y_milieu)


class TroisPoints:
    def __init__(self, point1, point2, point3):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3

    @property
    def point1(self):
        return self.__point1

    @point1.setter
    def point1(self, value):
        self.__point1 = value

    @property
    def point2(self):
        return self.__point2

    @point2.setter
    def point2(self, value):
        self.__point2 = value

    @property
    def point3(self):
        return self.__point3

    @point3.setter
    def point3(self, value):
        self.__point3 = value

    def sont_alignes(self):
        distance1 = self.__point1.calculer_distance(self.__point2)
        distance2 = self.__point1.calculer_distance(self.__point3)
        distance3 = self.__point2.calculer_distance(self.__point3)
        return (
            distance1 == distance2 + distance3
            or distance2 == distance1 + distance3
            or distance3 == distance1 + distance2
        )

    def est_isocèle(self):
        distance1 = self.__point1.calculer_distance(self.__point2)
        distance2 = self.__point1.calculer_distance(self.__point3)
        distance3 = self.__point2.calculer_distance(self.__point3)
        return distance1 == distance2 or distance1 == distance3 or distance2 == distance3
    

point = Point(3,2)
print(point)
#print(point.calculer_distance(Point(-5,0)))
#print(point.calculer_milieu(Point(3,5)))
print()
point2 = Point(4,2)
print(point2)
print("Equal:",point == point2)