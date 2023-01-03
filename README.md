# Closest-Pair

Algorithm: 
1.	We create a special type called Point to represent the points that we are finding the closest pair for. 
2.	The repr function tells how to graphically represent the new type created under Point. 
3.	Main function creates a list called points containing n random Point objects that we have to find the closest pair from. 
4.	After sorting according to the x coordinate of the Point we start to split the list into two halves (left and right). This is done from the median n/2. This is repeated recursively until the base case is met (n = 2 or 3). 
5.	At list size 2 or 3, points are individually compared and the shortest distance is calculated. 
6.	The tree is again built back up as various closest pairs are compared. Ultimately closest pair between the right and left list individually is compared and stored in closest. 
7.	The distance of this closest value is used to define a horizontal slice of size 2d about the centre x. Here we try to find a pair between the right and left lists that is closer than the closest pair of the two lists taken separately. 
8.	If this is found closest_m becomes the closest pair else closest is the answer.

Time Complexity:
Every step we are dividing the problem size by 2 and hence the time complexity is O(log n) (recursion). In the slice loop we go over every point central bracket thus the total final complexity amounts to O (n log n). 

Proof of correctness:

def ClosestPair
Base Case: for n=2 and n=3 special conditions defined
Induction hypothesis: the algorithm can split a list of size n into two smaller lists of size n/2 roughly
Induction Step: It will continue to split smaller lists into smaller ones (it can split n/2 list into two lists of n/4). The splitting can never split a list into a list of size one because that would require the parent list to be of size 2 or 3 which would hit the base case.

Slicing loop
Basis: at the start, when we have considered no pairs, closest_m is none, none
Induction hypothesis: at some step n the invariant is held
Induction step: at step n+1, if the new distance of the new pair is less than closest_m, we overwrite closest_m with the new pair, thus maintaining the invariant.
