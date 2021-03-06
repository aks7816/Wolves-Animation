from cs1graphics import *
from time import sleep

#basic background

paper = Canvas(600,400, 'navy', 'Wolves at Night')
snow = Rectangle(600,200, Point(300,400))
snow.setFillColor('seashell')
snow.setBorderColor('seashell')
trunk = Rectangle(20, 260, Point(250,170))
trunk.setFillColor('brown')
trunk.setBorderColor('sienna')
trunk.setBorderWidth(3)
leaves = Circle(80, Point(250,100))
leaves.setFillColor('green')
leaves.setBorderColor('limegreen')
leaves.setBorderWidth(4)
dep = Path(Point(200, 100), Point(212, 120), Point(224, 100))
dep.setBorderColor('darkolivegreen')
dep.setBorderWidth(2)
dep1 = dep.clone()
dep1.move(80,0)
dep2 = dep.clone()
dep2.move(40, 10)
dep3 = dep.clone()
dep3.move(40, -40)
moon = Circle(50, Point(500, 70))
moon.setFillColor('floralwhite')
moon.setBorderColor('floralwhite')
moonEye = Ellipse(10,20, Point(470,65))
moonEye.setBorderColor('dimgrey')
moonPupil = Circle(5, Point(470, 70))
moonPupil.setFillColor('black')
moonCovering = Circle(50, Point(530,70))
moonCovering.setFillColor('navy')
moonCovering.setBorderColor('navy')
paper.add(snow)
paper.add(trunk)
paper.add(leaves)
paper.add(dep)
paper.add(dep1)
paper.add(dep2)
paper.add(dep3)
paper.add(moon)
paper.add(moonCovering)
paper.add(moonEye)
paper.add(moonPupil)


#Animal layer

animal = Layer()
leg1 = Rectangle(10,76, Point(5,75))
leg1.adjustReference(0,-15)
leg1.setFillColor('dimgrey')
leg1.setBorderColor('dimgrey')
leg2 = leg1.clone()
leg1.move(90,0)
body = Ellipse(120,60,Point(50,55))
body.setFillColor('dimgrey')
body.setBorderColor('dimgrey')
tail = Circle(10, Point(-10, 55))
tail.setFillColor('dimgrey')
tail.setBorderColor('dimgrey')
head = Circle(27, Point(100,20))
head.setFillColor('dimgrey')
head.setBorderColor('dimgrey')
ear1 = Polygon(Point(74,10), Point(76,-20), Point(95,-5))
ear1.setFillColor('dimgrey')
ear1.setBorderColor('dimgrey')
ear2 = ear1.clone()
ear2.flip()
ear2.move(47,0)
eye1 = Ellipse(8, 12, Point(90, 18))
eye1.setFillColor('white')
eye2 = eye1.clone()
eye2.move(18,0)
pupil1 = Circle(2, Point(90,20))
pupil1.setFillColor('black')
pupil2 = pupil1.clone()
pupil2.move(18,0)
animal.add(leg1)
animal.add(leg2)
animal.add(body)
animal.add(tail)
animal.add(head)
animal.add(ear1)
animal.add(ear2)
animal.add(eye1)
animal.add(eye2)
animal.add(pupil1)
animal.add(pupil2)
animal.move(80,200)
sleep(1)
paper.add(animal)
sleep(1)
animal.rotate(-30)
sleep(1)
animal.rotate(30)


twin = animal.clone()
twin.flip()
twin.move(280,0)
paper.add(twin)
sleep(1)
greeting = Text("Wanna play in the snow?")
greeting.setFontSize(30)
greeting.move(200,370)
paper.add(greeting)
sleep(1)
paper.remove(greeting)
sleep(1)
greeting1 = Text("No, it's ok! Have fun!!")
greeting1.setFontSize(30)
greeting1.move(300,370)
paper.add(greeting1)
sleep(1)
paper.remove(greeting1)
sleep(1)
animal.flip()
sleep(1)
twin.move(40,0)
sleep(1)
paper.remove(animal)
sleep(1)
twin.flip()
sleep(1)
twin.move(60,0)
paper.remove(twin)


