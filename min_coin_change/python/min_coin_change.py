###########################################################################################################################
#Recursive Implementation of Minimum Coin Number Problem - http://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/
#Time Complexity: O(nlog(n))
###########################################################################################################################

def reduce (amount, coins, change):
	if (amount == 0):
		return (change);
	if (coins [-1] > amount):
		return (reduce (amount, coins [ : -1], change));
	return (reduce (amount - coins [-1], coins, change + [coins [-1]]));

#Input: Line 1 - Amount, Line 2 - List Space separated integers representing the coin values
amount = int (input ());
coins = sorted ([int (i) for i in input ().split ()]);

#Sample call to reduce () - The 3rd argument must always be an empty list (it is used in recursion)
change = reduce (amount, coins, []);
print (change, len (change));