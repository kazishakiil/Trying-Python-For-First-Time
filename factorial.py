1.	n_terms = int(input ("How many terms the user wants to print "))  
2.	  
3.	# First two terms  
4.	n_1 = 0  
5.	n_2 = 1  
6.	count = 0  
7.	  
8.	# Now, we will check if the number of terms is valid or not  
9.	if n_terms <= 0:  
10.	    print ("Please enter a positive integer, the given number is not valid")  
11.	# if there is only one term, it will return n_1  
12.	elif n_terms == 1:  
13.	    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
14.	    print(n_1)  
15.	# Then we will generate Fibonacci sequence of number  
16.	else:  
17.	    print ("The fibonacci sequence of the numbers is:")  
