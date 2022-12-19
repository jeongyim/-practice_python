import polyArea
print(polyArea.rectangleArea(3,3))
print(polyArea.triangleArea(3,3))
print(polyArea.circlreArea(3))

import polyArea as pa
print(pa.rectangleArea(3,3))
print(pa.triangleArea(3,3))
print(pa.circlreArea(3))

from polyArea import *
print(rectangleArea(3,3))
print(triangleArea(3,3))
print(circlreArea(3))

from polyArea import rectangleArea, triangleArea, circlreArea
print(rectangleArea(3,3))
print(triangleArea(3,3))
print(circlreArea(3))

from polyArea import rectangleArea as pr, triangleArea as pt, circlreArea as pc
print(pr(3,3))
print(pt(3,3))
print(pc(3))