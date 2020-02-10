from display import *
from draw import *
from random import randint
from math import sqrt

s = new_screen()
YELLOW = [225,225,64]
WHITE = [255,255,255]
CONNECT = [93,93,28]
large_stars,small_stars = [],[]
large_stars.append([(-6,0,YELLOW),(-4,0,YELLOW),(-3,0,YELLOW),(-2,0,YELLOW),(-1,0,WHITE),
                    (0,0,WHITE),(1,0,WHITE),(2,0,YELLOW),(3,0,YELLOW),(4,0,YELLOW),(6,0,YELLOW),
                    (0,-8,YELLOW),(0,-7,YELLOW),(0,-5,YELLOW),(0,-4,YELLOW),(0,-3,YELLOW),(0,-2,YELLOW),(0,-1,WHITE),
                    (0,1,WHITE),(0,2,YELLOW),(0,3,YELLOW),(0,4,YELLOW),(0,5,YELLOW),(0,7,YELLOW),(0,8,YELLOW),
                    (-2,-1,YELLOW),(-1,-2,YELLOW),(-1,-1,YELLOW),
                    (-2,1,YELLOW),(-1,2,YELLOW),(-1,1,YELLOW),
                    (2,-1,YELLOW),(1,-2,YELLOW),(1,-1,YELLOW),
                    (2,1,YELLOW),(1,2,YELLOW),(1,1,YELLOW)])
large_stars.append([(-4,0,YELLOW),(-3,0,YELLOW),(-2,0,YELLOW),(-1,0,WHITE),
                    (0,0,WHITE),(1,0,WHITE),(2,0,YELLOW),(3,0,YELLOW),(4,0,YELLOW),
                    (0,-6,YELLOW),(0,-5,YELLOW),(0,-4,YELLOW),(0,-3,YELLOW),(0,-2,YELLOW),(0,-1,WHITE),
                    (0,1,WHITE),(0,2,YELLOW),(0,3,YELLOW),(0,4,YELLOW),(0,5,YELLOW),(0,6,YELLOW),
                    (-2,-1,YELLOW),(-1,-3,YELLOW),(-1,-2,YELLOW),(-1,-1,YELLOW),
                    (-2,1,YELLOW),(-1,3,YELLOW),(-1,2,YELLOW),(-1,1,YELLOW),
                    (2,-1,YELLOW),(1,-3,YELLOW),(1,-2,YELLOW),(1,-1,YELLOW),
                    (2,1,YELLOW),(1,3,YELLOW),(1,2,YELLOW),(1,1,YELLOW)])
small_stars.append([(-3,0,YELLOW),(-2,0,YELLOW),(-1,0,YELLOW),(1,0,YELLOW),(2,0,YELLOW),(3,0,YELLOW),
                    (0,-3,YELLOW),(0,-2,YELLOW),(0,-1,YELLOW),(0,1,YELLOW),(0,2,YELLOW),(0,3,YELLOW),
                    (-2,-1,YELLOW),(-1,-2,YELLOW),(-1,-1,YELLOW),(-2,1,YELLOW),(-1,2,YELLOW),(-1,1,YELLOW),
                    (2,-1,YELLOW),(1,-2,YELLOW),(1,-1,YELLOW),(2,1,YELLOW),(1,2,YELLOW),(1,1,YELLOW)])
small_stars.append([(-3,0,YELLOW),(-2,0,YELLOW),(-1,0,YELLOW),(0,0,YELLOW),(1,0,YELLOW),(2,0,YELLOW),(3,0,YELLOW),
                    (0,-3,YELLOW),(0,-2,YELLOW),(0,-1,YELLOW),(0,1,YELLOW),(0,2,YELLOW),(0,3,YELLOW),
                    (-1,-1,YELLOW),(-1,1,YELLOW),(1,-1,YELLOW),(1,1,YELLOW)])
small_stars.append([(-3,0,YELLOW),(-2,0,YELLOW),(-1,0,YELLOW),(0,0,YELLOW),(1,0,YELLOW),(2,0,YELLOW),(3,0,YELLOW),
                    (0,-3,YELLOW),(0,-2,YELLOW),(0,-1,YELLOW),(0,1,YELLOW),(0,2,YELLOW),(0,3,YELLOW),
                    (-2,-2,YELLOW),(-2,2,YELLOW),(2,-2,YELLOW),(2,2,YELLOW)])
small_stars.append([(-2,0,YELLOW),(-1,0,YELLOW),(0,0,YELLOW),(1,0,YELLOW),(2,0,YELLOW),
                    (0,-2,YELLOW),(0,-1,YELLOW),(0,1,YELLOW),(0,2,YELLOW),
                    (-1,-1,YELLOW),(-1,1,YELLOW),(1,-1,YELLOW),(1,1,YELLOW)])
small_stars.append([(-2,0,YELLOW),(-1,0,YELLOW),(1,0,YELLOW),(2,0,YELLOW),
                    (0,-2,YELLOW),(0,-1,YELLOW),(0,1,YELLOW),(0,2,YELLOW),
                    (-1,-1,YELLOW),(-1,1,YELLOW),(1,-1,YELLOW),(1,1,YELLOW)])
small_stars.append([(-2,0,YELLOW),(-1,0,YELLOW),(0,0,YELLOW),(1,0,YELLOW),(2,0,YELLOW),
                    (0,-2,YELLOW),(0,-1,YELLOW),(0,1,YELLOW),(0,2,YELLOW)])
small_stars.append([(-2,0,YELLOW),(-1,0,YELLOW),(1,0,YELLOW),(2,0,YELLOW),
                    (0,-2,YELLOW),(0,-1,YELLOW),(0,1,YELLOW),(0,2,YELLOW)])
small_stars.append([(-1,0,YELLOW),(0,0,YELLOW),(1,0,YELLOW),
                    (0,-2,YELLOW),(0,-1,YELLOW),(0,1,YELLOW),(0,2,YELLOW)])
small_stars.append([(-1,0,YELLOW),(0,0,YELLOW),(1,0,YELLOW),
                    (0,-1,YELLOW),(0,1,YELLOW)])
small_stars.append([(-1,0,YELLOW),(1,0,YELLOW),(0,-1,YELLOW),(0,1,YELLOW)])
small_stars.append([(0,0,YELLOW)])

def summation(num):
    return int(num * (num + 1) / 2)

class Star:
    def __init__(self,type="large"):
        center_x = randint(10,XRES-10)
        center_y = randint(10,YRES-10)
        self.center = (center_x,center_y)
        self.points = []
        if type == "large":
            random = randint(0,1)
            for point in large_stars[random]:
                self.points.append((center_x + point[0],center_y + point[1],point[2]))
        else:
            total_sum = summation(len(small_stars))
            random = randint(1,total_sum)
            for index in range(0,len(small_stars)):
                if summation(index + 1) >= random:
                    for point in small_stars[index]:
                        self.points.append((center_x + point[0],center_y + point[1],point[2]))
                    break
        self.points.sort()
    def plot(self):
        for point in self.points:
            plot(s,point[2],point[0],point[1])

def in_other_stars(points,star):
    for point_A in points:
        for point_B in star.points:
            if point_A[0] == point_B[0]:
                if point_A[1] == point_B[1]:
                    return True
    return False

def distance(A,B):
    return sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)

class Constellation:
    def __init__(self):
        self.stars = []
        self.points = []
        center_star = Star()
        self.stars.append(center_star)
        self.points.extend(center_star.points)
        for i in range(70):
            self.add()
    def add(self):
        new_star = Star("small")
        while in_other_stars(self.points,new_star):
            new_star = Star("small")
        self.stars.append(new_star)
        self.points.extend(new_star.points)
        self.points.sort()
    def plot(self):
        if len(self.stars) > 1:
            for star in self.stars:
                other_stars = filter(lambda x : x != star, self.stars)
                # other_star = min(other_stars,key=lambda x: distance(x.center,star.center))
                other_stars.sort(key=lambda x: distance(x.center,star.center))
                random = randint(0,3)
                if random == 3:
                    other_star = other_stars[1]
                    draw_line(star.center[0],star.center[1],other_star.center[0],other_star.center[1],s,CONNECT)
                other_star = other_stars[0]
                draw_line(star.center[0],star.center[1],other_star.center[0],other_star.center[1],s,CONNECT)
        for star in self.stars:
            star.plot()

Constellation().plot()
for i in range(65):
    Star("small").plot()
print("In binary.ppm,ascii.ppm,img.png!")

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
