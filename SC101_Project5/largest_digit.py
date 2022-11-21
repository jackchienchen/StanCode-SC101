"""
File: largest_digit.py
Name: Jack Chen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: integers to be examined.
	:return: Return the largest single digit in the input n.
	"""''
	# Set a variable for maximum digit.
	max_word = 0
	# square root to make sure the input will be a positive number.
	n = int((n**2)**0.5)
	return find_largest_digit_helper(n, max_word)


def find_largest_digit_helper(n, max_word):
	if n == 0:  # BASE CASE! When there's no more digit to compare in n.
		return max_word
	else:
		last_word = n - 10*(n//10)  # To pop the single digit
		if last_word > max_word:  # When last_word is larger than the max_word
			max_word = last_word
		# Recursion with n without its single digit, and carrying the maximum digit.
		return find_largest_digit_helper(n//10, max_word)


if __name__ == '__main__':
	main()
