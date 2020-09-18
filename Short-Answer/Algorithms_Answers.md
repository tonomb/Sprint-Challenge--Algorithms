#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) this code snippet has a runtime of O(n) . The snippet is a linear runtime because I am assuming that the amount of times the while loop many runs is entirely dependant on the value passes in as n


b) This code snippet has a runtime of O(n^2). This is because it has a for loop dependent on N which makes that line run at O(n) and nested inside of that loop there is a while loop dependnt on the value of n which makes that line of code run at O(n).   Both those lines are dependant on N, if N increases, the number of computatios will also increase.  Since the while loop is nested the final runtime si O(n^2) 


c) This recursive snippet is O(n). the function is calculating the number of bunny ears recursively which means that the amount of recursive calls that the algorythm makes will depend on the number of bunnies passed in. Since the number of operations is tied to the number of bunnies the larger the input the more calls that will be made making it run at a linear time.  

## Exercise II

? How do you calculate F braking the less amount of eggs. 

I propose that we could calulate f using a implementation of binary search.  Since the number of floores will always increase we can model the building like a sorted array of numbers incrementing 1 x 1 = [ 1,2,3,4,5,6,7, 8 ,9 ,10].  We are also searching for a floor that if dropped higher will break the eggs and dropped lower won't break the egg. This looks a lot like the middlepoint of the binary search. 

Since we are using binary search we could asume that the runtime would be O(log(n))