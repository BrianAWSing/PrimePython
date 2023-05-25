#Licence: MIT
#
#Author(s): Brian Byrne
#
#Program purpose:
#----------------
# 
# Display all the prime numbers between 1 to 250.
# Store the results in a results.txt file.
#
#Program notes:
#--------------
#
# Define the upper limit to calculate to, then create 
# an array of boolean for that number.
#
# We assume it is prime unless it fails our test then we
# change the value to False
#
#--------------------------------------------------------
upperLimit=250
#
prime_array=[True]*(upperLimit+1)
#
countToUpper=1
#
# Two loops, one to the upper limit (ie. 250)
# Another to compare the current number with previous
# mod them and if 0 then not prime, continue on
#
while countToUpper<upperLimit+1:
    countToUpper = countToUpper+1
    for innerCheck in range(2,countToUpper):
        x=(countToUpper % innerCheck)
        if x==0:
            prime_array [countToUpper]=False
#
# At this point we have an array stuffed full of boolean values 
# and we print only the True ones
# 
for i in range(upperLimit):
    if prime_array[i] :
        print (i)
#
# Open a file and print them there.
#
#
filename = "results.txt"
#
with open(filename , 'w') as fileToWrite:
	for j in range(2, upperLimit):
    		if prime_array[j] :
        		fileToWrite.write("\n"+str(j))