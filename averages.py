#Week3-Avg:
#Using a for loop and range, calculate the mean of all of the numbers between 1 and 20 (including 1 and 20!). 
#Do the same thing without a loop with fewer lines of code (HINT: might have to use a command in a module)
#Try to make your code clean

sum=0
i=1
while i<=20:
	print(i)
	sum+=i
	i+=1
average=sum/20

#vs
# using the statistics module
# import statistics
# average=statistics.mean(range(1,21))
# print(average) ----> 10.5
