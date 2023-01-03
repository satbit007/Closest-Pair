import random
import math

# Creates a class for representing a point in 2D space.
class Point():
  # Constructor, takes in x and y
  def _init_(self, x, y):
    self.x = x
    self.y = y
    
  # Tells python how to represent a point as text
  def _repr_(self):
    return f"({self.x}, {self.y})"

def distance(a,b):
  return math.sqrt((a.x-b.x)*2+(a.y-b.y)*2)

def main():
  # create a shuffled list of length n
  n = 20
  points = [Point(random.randint(0,100), random.randint(0,100)) for i in range(n)]
  # The key is a higher order function that defines the basis on which comparisons should happen in the sort (x coord)
  points = sorted(points, key = lambda p : p.x)
  
  closest = ClosestPair(points)
  print(points)
  print(closest)

def ClosestPair(points):
  n = len(points)
  
  # base case
  if(n == 3):
    p1 = points[0]
    p2 = points[1]
    p3 = points[2]
    pairs = [(p1,p2,distance(p1,p2)), (p2,p3,distance(p2,p3)), (p3,p1,distance(p3,p1))]
    return min(pairs, key=lambda p: p[2])

  # base case
  if(n == 2):
    return (points[0], points[1], distance(points[0],points[1]))
  
  # Finds the closest pair in the left half of the points array recursively 
  closest_l = ClosestPair(points[0:n//2])

  # Finds the closest pair in the right half of the points array recursively
  closest_r = ClosestPair(points[n//2:n])

  # Finds the closest pair out of the two closest pairs in the left and right side taken in isolation
  closest = min(closest_l, closest_r, key = lambda c : c[2])

  # THis is the distance of the closest pair
  d = closest[2]
  # THis is the center point of all the points
  x = points[n//2 - 1].x

  # WE add all points within the x-coordinates, x - d and x + d to the slice array
  slice = []
  for p in points:
    if(p.x >= x - d and p.x <= x + d):
      slice.append(p)
  
  # We sort slice on the basis of the y components of the points
  slice = sorted(slice, key = lambda p: p.y)
  ns = len(slice)
  # IT is not possible to exceed a distance of 30000 in a 100x100 grid, since 100sqrt(2) < 30000, thus it is a good dummy value
  closest_m = (None, None, 30000)

  # Find the closest pair in the slice x - d, x + d
  # inv: i < ns, j < ns, closest_m is the closest pair that we have considered so far
  # basis: at the start, when we have considered no pairs, closest_m is none, none
  # induction hypothesis, at some step n the invariant is held
  # indcution step: at step n+1, if the new distance of the new pair is less than closest_m, we overwrite closest_m with the new pair, thus maintaining the invariant
  for i in range(ns):
    for j in range(i + 1, min(ns, i+8)):
      dist = distance(slice[i], slice[j])
      if(dist < closest_m[2]):
        closest_m = (slice[i],slice[j], dist)
  #from inv 1 and 2, we know that the loop goes over every possible pair of vertices, thus, since we have also proven that the third invariant is held
  # at the end of the loop, we will have the closest pair through the middle held in closest_m
  
  # Return the closest pair out of the closest pair of the left and right side taken in isolation and the closest pair through the middle slice
  return min(closest, closest_m, key = lambda c : c[2])

main()
