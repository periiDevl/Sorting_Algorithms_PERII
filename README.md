# Sorting algorithms

lately I have been thinking of this problem, if you have a 1000000 different random numbers in a list you had to sort them from the least to the greatest in the smallest amount of processing time, how would you do that? well in today’s video we will create 5 different sorting algorithms to solve this issue.

—-------------------------------------------------------------------------------------------------------------------
The first algorithm we will try to use is the bubble sort algorithm, The bubble sort algorithm
from all the algorithms this is the simplest but the slowest one. lets visualsize our list in columns so 4 8 1 7

look at 4 and 8 because we are try to get greatest to least we will swap there places to get
8 4 1 and 7

4 is bigger then one
1 is less then 7 so we swap the colloms again so now at the end of the interation our list looks like this with 8471 but the list is still not sorted so we have to iterate over it a second time
so after doing the same for the second iteration we got a sorted list! (8741)

before we move on there is a way we can measure your algorithms (time complexity)
in our case the time complexity is O(n^2)

this means the more you stuff you input to the algorithm how much it will effect the speed of the algorithm for example 

my_array = [1, 2, 3, 4, 5]

for num in my_array:
    print(num)

this code is in the time complexity of O(n), O(n) is a linear time complexity so if we input into this array more inputs the speed will go down linearly the more you add to the list

—--------------------------------------------------------------------------------------------------------------------

The bubble algorithm is fine but when you have a lot more numbers to sort through it becomes really slow because of its time complexity.

A faster algorithm we will implement is the insertion algorithm.


here is our array [9,3,4,6]
similar to the bubble sort algorithm we will compare 9 and 3, 9 is bigger so we will not change anything
[9, 3, 4, 6]
next we have 4 we will compare the 4 to 9 and 3 and put it between them
[9, 4, 3, 6]
now to 6 we will compare 6 to its neighbors and we can sort it into the right place
[9, 6, 4, 3]
and our array is sorted

on our time complexity graph is O(n^2), but how can it be also O(n^2) if we we know its faster then the bubble sort algorithm? well time complexity is not a representation of the overall speed its only demonstrating the way the more inputs will slow the algorithm. well lets move to the next algorithm.

Selection sort.

here is our array [2, 8, 5, 1]

Lets visualize Selection sort with a current item and the maximum item
we will set our first value (2) in the array as the maximum and we will to find a bigger number then the our current maximum
[2, 8, 5, 1]
here we found 8 as so we will move the 8 as the fist member of the array
[8, 2,5, 1]
now we can count 8 as sorted and we will set 2 as our current maximum
[8, 2, 5, 1]
here we found 5 as our bigger maximum so we will swap it with 2
[8, 5, 2, 1]
now 5 is sorted and we can see the array is already sorted for us!

selection sort also has the time complexity of O(n^2) and according to google its not as fast as selection sort, when I tried it the selection sort was way faster but maybe its just and issue in my code or something 

—----------------------------------------------------------------------------------------------------------------
next we have 2 of my favorite algorithms

Lets start with the merge algorithm unlike our proviese algorithms this algorithm is implemented recursively.
The merge sort algorithm by taking a big problem and separating it into small problems that are easier to deal with

[9, 5, 3 , 2 , 7, 10]
now we separate the array in half until we get the individual numbers
now we will take the items and merge them into arrays

[9, 5] [3, 2]...
now merge again but in the correct order
[9, 5, 3][10, 7, 2]
merge again
[10, 9, 7, 5, 3, 2]
and we have our sorted array!

the time complexity of merge sort is O(n * logn) which is better then O(n^2) sense it is closer to linear time at quaslinear time

—-----------------------------------------------------------------------------------------------------------------------
Now to the last algorithm 
Radix sort works by looking at the the sections of the numbers
so here is our array [192, 24, 65, 3]
lets look at the first section
[65, 24, 3, 192]
now lets look at the second section
[192, 65, 24, 3]
now at the third section
and our array is sorted!
—------------------------------------------------------------------------------------------------------------------------
well that all the algorithms I created to sort my big list of a million numbers, if you want to try these or use them in your projects you can go to the description and download a demo that showcases them and my github to steal the functions if you want to
